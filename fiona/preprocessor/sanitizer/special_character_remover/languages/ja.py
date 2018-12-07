import re


regex = r'[^ぁ-ゟ゠-ヿ㐀-䶵一-鿋豈-頻⺀-⿕]+'


def special_character_remover(text: str) -> str:
    return re.compile(regex).sub('', text)
