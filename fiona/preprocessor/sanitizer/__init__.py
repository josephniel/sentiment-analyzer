import re

from fiona.preprocessor.sanitizer.special_character_remover import (
    remove_special_characters
)


def sanitize_text(text: str, language_code: str) -> str:
    text = _remove_unedited_sequence(text)
    text = _trim_text(text)
    text = _remove_html_tags(text)
    text = remove_special_characters(
        language_code=language_code,
        text=text
    )
    return text.lower().strip()


def _remove_unedited_sequence(text: str) -> str:
    return re.sub(r'\[\[\[(.*)\]\]\]', '', text)


def _trim_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text)


def _remove_html_tags(text: str) -> str:
    return re.sub(r'<.*?>', '', text)
