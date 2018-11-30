from enum import Enum
from typing import NamedTuple


class ReservedWordsEnum(Enum):
    PAD = '<PAD>'
    UNUSED = '<UNUSED>'


class LanguageText(NamedTuple):
    language_code: str
    text: str
