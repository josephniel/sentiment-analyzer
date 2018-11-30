from difflib import SequenceMatcher
from typing import Dict, Tuple

import re

from fiona.types import LanguageText, ReservedWordsEnum


class TranslationSanitizer:

    special_character_regex: Dict[str, str] = {}

    def sanitize(
            self,
            original: LanguageText,
            translation: LanguageText,
    ) -> Tuple[LanguageText, LanguageText]:

        original_text = self._remove_unedited_sequence(original.text)
        translation_text = self._remove_unedited_sequence(translation.text)

        original_text = self._trim_text(original_text)
        translation_text = self._trim_text(translation_text)

        original_text = self._remove_html_tags(original_text)
        translation_text = self._remove_html_tags(translation_text)

        # original_text, translation_text = self._update_untranslated_text(
        #     original_text=original_text,
        #     translation_text=translation_text,
        # )

        original_text = self._remove_special_characters(
            language_code=original.language_code,
            text=original_text
        )
        translation_text = self._remove_special_characters(
            language_code=translation.language_code,
            text=translation_text
        )

        return LanguageText(
            text=original_text,
            language_code=original.language_code,
        ), LanguageText(
            text=translation_text,
            language_code=translation.language_code,
        )

    def _remove_unedited_sequence(self, string: str) -> str:
        return re.sub(r'\[\[\[(.*)\]\]\]', '', string)

    def _trim_text(self, string: str) -> str:
        return re.sub(r'\s+', ' ', string.strip())

    def _remove_html_tags(self, string: str) -> str:
        return re.sub(r'<.*?>', '', string)

    def _update_untranslated_text(
            self,
            original_text: str,
            translation_text: str,
    ) -> Tuple[str, str]:
        s = SequenceMatcher(None, original_text, translation_text)
        for match in s.get_matching_blocks():
            original_text = self._replace_untranslated_word(
                string=original_text,
                start_index=match.a,
                size=match.size
            )
            translation_text = self._replace_untranslated_word(
                string=translation_text,
                start_index=match.b,
                size=match.size
            )
        return original_text, translation_text

    def _replace_untranslated_word(
            self,
            string: str,
            start_index: int,
            size: int,
    ) -> str:
        start = string[0:start_index-1]
        end = string[start_index+size+1:]
        return f'{start}{ReservedWordsEnum.UNUSED.value}{end}'

    def _remove_special_characters(
            self,
            language_code: str,
            text: str
    ) -> str:
        regex = TranslationSanitizer.special_character_regex.get(language_code)
        if not regex:
            return text
        return re.compile(regex).sub('', text)
