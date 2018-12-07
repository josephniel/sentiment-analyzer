from typing import Callable, Dict, List

from fiona.preprocessor.tokenizer.languages.en import tokenize as en_tokenizer
from fiona.preprocessor.tokenizer.languages.ja import tokenize as ja_tokenizer


tokenizer_list: Dict[str, Callable] = {
    'en': en_tokenizer,
    'ja': ja_tokenizer,
}


def tokenize_text(text: str, language_code: str) -> List[str]:
    tokenizer = tokenizer_list.get(language_code)
    if not tokenizer:
        return []
    return tokenizer(text)
