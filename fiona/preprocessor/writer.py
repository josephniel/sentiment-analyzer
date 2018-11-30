from contextlib import contextmanager
from typing import Iterator

import csv
import os
import sys


class CSVWriter:

    @staticmethod
    @contextmanager
    def write(filename: str) -> Iterator:
        csv.field_size_limit(sys.maxsize)
        current_file_directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f'../../dataset/sanitized/{filename}'
        )
        with open(current_file_directory, mode='w') as f:
            yield csv.writer(f, quoting=csv.QUOTE_ALL)
