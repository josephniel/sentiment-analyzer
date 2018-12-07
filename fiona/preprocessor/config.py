import os


ORIGINAL_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../dataset/original/'
)
SANITIZED_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../dataset/sanitized/'
)
TOKENIZED_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../dataset/tokenized/'
)
VECTORIZED_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../dataset/vectorized/'
)
WORD_INDEX_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../../dataset/indices/'
)
