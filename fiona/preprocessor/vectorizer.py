import os

from typing import Dict, List

from fiona.preprocessor.config import WORD_INDEX_FILE_PATH
from fiona.preprocessor.reader import csv_reader
from fiona.preprocessor.writer import csv_writer


class TextVectorizer:

    current_word_index: Dict[str, int]
    language_code: str
    word_index_size: int = 0

    def __init__(self, language_code: str) -> None:
        self.language_code = language_code

        read_path = os.path.join(WORD_INDEX_FILE_PATH, f'{language_code}.csv')
        with csv_reader(read_path) as reader:
            self.current_word_index = {}
            for line in reader:
                self.current_word_index[line[0]] = line[1]
                self.word_index_size = line[1]

    def vectorize_list(self, text_list: List[str]) -> List[int]:
        return list(map(self._get_word_index, text_list))

    def _get_word_index(self, text: str) -> int:
        index = self.current_word_index.get(text)
        if not index:
            self.word_index_size = self.word_index_size + 1
            self.current_word_index[text] = self.word_index_size
            index = self.word_index_size
        return index

    def save_updated_word_index(self) -> None:
        write_path = os.path.join(
            WORD_INDEX_FILE_PATH,
            f'{self.language_code}.csv'
        )
        with csv_writer(write_path) as writer:
            for key, value in self.current_word_index.items():
                writer.writerow([key, value])
