from tensorflow import keras, nn, train


def create_model(vocab_size=10000):
    model = keras.Sequential()

    model.add(keras.layers.Embedding(vocab_size, 16))
    model.add(keras.layers.GlobalAveragePooling1D())
    model.add(keras.layers.Dense(16, activation=nn.relu))
    model.add(keras.layers.Dense(1, activation=nn.sigmoid))

    model.compile(
        optimizer=train.AdamOptimizer(),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model
