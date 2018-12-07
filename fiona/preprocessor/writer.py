from contextlib import contextmanager
from typing import Iterator

import csv
import sys


@contextmanager
def csv_writer(current_file_directory: str) -> Iterator:
    csv.field_size_limit(sys.maxsize)
    with open(current_file_directory, 'w') as f:
        yield csv.writer(f, quoting=csv.QUOTE_ALL)
