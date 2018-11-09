from tensorflow import keras


def preprocess_data(dataset, train_data, test_data):
    word_index = dataset.get_word_index()

    word_index = {
        k: (v+3) for k, v in word_index.items()
    }
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2  # unknown
    word_index["<UNUSED>"] = 3

    train_data = keras.preprocessing.sequence.pad_sequences(
            train_data,
            value=word_index["<PAD>"],
            padding='post',
            maxlen=256
    )

    test_data = keras.preprocessing.sequence.pad_sequences(
            test_data,
            value=word_index["<PAD>"],
            padding='post',
            maxlen=256
    )

    return train_data, test_data
