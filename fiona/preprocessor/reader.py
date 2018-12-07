from contextlib import contextmanager
from typing import Iterator

import csv
import sys


@contextmanager
def csv_reader(current_file_directory: str) -> Iterator:
    csv.field_size_limit(sys.maxsize)
    with open(current_file_directory, "r") as f:
        yield csv.reader(f)
