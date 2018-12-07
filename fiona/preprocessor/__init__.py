import ast
import os

from fiona.preprocessor.config import (
    ORIGINAL_FILE_PATH,
    SANITIZED_FILE_PATH,
    TOKENIZED_FILE_PATH,
    VECTORIZED_FILE_PATH,
)
from fiona.preprocessor.reader import csv_reader
from fiona.preprocessor.sanitizer import sanitize_text
from fiona.preprocessor.tokenizer import tokenize_text
from fiona.preprocessor.vectorizer import TextVectorizer
from fiona.preprocessor.writer import csv_writer


class TranslationPreprocessor:
    def process(
            self,
            filename: str,
            source: str,
            target: str,
    ) -> str:
        self._sanitize_translations(filename, source, target)
        self._tokenize_translations(filename, source, target)
        return self._vectorize_translations(filename, source, target)

    def _sanitize_translations(
            self,
            filename: str,
            source: str,
            target: str,
    ) -> None:
        i = 0
        read_path = os.path.join(ORIGINAL_FILE_PATH, filename)
        write_path = os.path.join(SANITIZED_FILE_PATH, filename)
        with csv_reader(read_path) as reader, csv_writer(write_path) as writer:
            for line in reader:
                sanitized_original = sanitize_text(
                    text=line[0],
                    language_code=source,
                )
                sanitized_translation = sanitize_text(
                    text=line[1],
                    language_code=target
                )
                writer.writerow([
                    sanitized_original,
                    sanitized_translation,
                    line[2]
                ])
                i = i + 1
                if i == 10:
                    break

    def _tokenize_translations(
            self,
            filename: str,
            source: str,
            target: str,
    ) -> None:
        read_path = os.path.join(SANITIZED_FILE_PATH, filename)
        write_path = os.path.join(TOKENIZED_FILE_PATH, filename)
        with csv_reader(read_path) as reader, csv_writer(write_path) as writer:
            for line in reader:
                tokenized_original = tokenize_text(
                    text=line[0],
                    language_code=source,
                )
                tokenized_translation = tokenize_text(
                    text=line[1],
                    language_code=target
                )
                writer.writerow([
                    str(tokenized_original),
                    str(tokenized_translation),
                    line[2]
                ])

    def _vectorize_translations(
            self,
            filename: str,
            source: str,
            target: str,
    ) -> str:
        original_vectorizer = TextVectorizer(source)
        translated_vectorizer = TextVectorizer(target)

        read_path = os.path.join(TOKENIZED_FILE_PATH, filename)
        write_path = os.path.join(VECTORIZED_FILE_PATH, filename)
        with csv_reader(read_path) as reader, csv_writer(write_path) as writer:
            for line in reader:
                vectorized_original = original_vectorizer.vectorize_list(
                    text_list=ast.literal_eval(line[0])
                )
                vectorized_translation = translated_vectorizer.vectorize_list(
                    text_list=ast.literal_eval(line[1])
                )
                writer.writerow([
                    str(vectorized_original),
                    str(vectorized_translation),
                    line[2]
                ])

        original_vectorizer.save_updated_word_index()
        translated_vectorizer.save_updated_word_index()

        return write_path
