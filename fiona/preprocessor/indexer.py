from typing import Dict, List

from fiona.types import LanguageText


class WordIndexer:

    supported_language_indexing: Dict[str, str] = {
        'en': ' ',
    }

    @staticmethod
    def index(
            current_word_list: List[str],
            language_text: LanguageText,
    ) -> List[str]:
        delimiter = WordIndexer.supported_language_indexing.get(
            language_text.language_code
        )
        if not delimiter:
            return current_word_list

        for word in language_text.text.split(delimiter):
            if word not in current_word_list:
                current_word_list.append(word)

        return current_word_list
