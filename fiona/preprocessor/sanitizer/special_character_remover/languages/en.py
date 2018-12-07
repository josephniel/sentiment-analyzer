import re


regex = r'[^a-zA-Z0-9 ]+'


def special_character_remover(text: str) -> str:
    return re.compile(regex).sub('', text)
