from typing import List

import tinysegmenter


def tokenize(text: str) -> List[str]:
    return tinysegmenter.TinySegmenter().tokenize(text)
