from typing import Dict, List

from fiona.types import LanguageText


class LanguageTextMutator:

    @staticmethod
    def mutate(
            language_text: LanguageText,
            word_index: Dict[str, int],
    ) -> List[int]:
        pass
