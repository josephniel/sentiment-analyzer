import re

from typing import List


def tokenize(text: str) -> List[str]:
    return re.split(r"\s+", text)
