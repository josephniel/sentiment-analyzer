from contextlib import contextmanager
from typing import Iterator

import csv
import os
import sys


class CSVReader:

    @staticmethod
    @contextmanager
    def read(filename: str) -> Iterator:
        csv.field_size_limit(sys.maxsize)
        current_file_directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            f'../../dataset/original/{filename}'
        )
        with open(current_file_directory, "r") as f:
            yield csv.reader(f)
