from typing import Dict

from .languages.en import (
    special_character_remover as en_special_character_remover
)
from .languages.ja import (
    special_character_remover as ja_special_character_remover
)


special_character_remover: Dict[str, str] = {
    'en': en_special_character_remover,
    'ja': ja_special_character_remover,
}


def remove_special_characters(language_code: str, text: str) -> str:
    remover = special_character_remover.get(language_code)
    if not remover:
        return text
    return remover(text)
