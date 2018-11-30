from typing import Dict, List, Tuple

from fiona.types import LanguageText
from fiona.preprocessor.indexer import WordIndexer
from fiona.preprocessor.mutator import LanguageTextMutator
from fiona.preprocessor.reader import CSVReader
from fiona.preprocessor.sanitizer import TranslationSanitizer
from fiona.preprocessor.writer import CSVWriter


class TranslationPreprocessor:

    original_word_list: List[str] = []
    translation_word_list: List[str] = []

    def process(
            self,
            filename: str,
            source: str,
            target: str,
    ) -> List[List[int]]:
        with CSVReader.read(filename) as reader, CSVWriter.write(filename) as writer:  # NOQA
            i = 0
            for line in reader:
                sanitized_original, sanitized_translation = (
                    self._prepare_translation_texts(
                        LanguageText(
                            text=line[0],
                            language_code=source,
                        ),
                        LanguageText(
                            text=line[1],
                            language_code=target
                        )
                    )
                )
                writer.writerow([
                    sanitized_original,
                    sanitized_translation,
                    line[2]
                ])
                i = i + 1
                if i == 10:
                    break

    def _prepare_translation_texts(
            self,
            original: LanguageText,
            translation: LanguageText,
    ) -> Tuple[str, str]:
        original, translation = TranslationSanitizer().sanitize(
            original=original,
            translation=translation,
        )

        self.original_word_list = WordIndexer.index(
            current_word_list=self.original_word_list,
            language_text=original,
        )
        self.translation_word_list = WordIndexer.index(
            current_word_list=self.translation_word_list,
            language_text=translation,
        )

        return original.text, translation.text

    def _mutate_language_text(
            self,
            language_text: LanguageText,
            word_index: Dict[str, int],
    ) -> List[int]:
        return LanguageTextMutator.mutate(
            language_text=language_text,
            word_index=word_index,
        )


if __name__ == "__main__":
    processor = TranslationPreprocessor()
    processor.process('en_ja_jobs.csv', 'en', 'ja')
