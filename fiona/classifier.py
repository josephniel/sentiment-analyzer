from tensorflow import keras

from fiona.preprocessor import preprocess_data
from fiona.model import create_model


imdb = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = (
    imdb.load_data(num_words=10000)
)

train_data, test_data = preprocess_data(imdb, train_data, test_data)

x_val = train_data[:10000]
partial_x_train = train_data[10000:]

y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]


model = create_model()

history = model.fit(
    partial_x_train,
    partial_y_train,
    epochs=40,
    batch_size=512,
    validation_data=(x_val, y_val),
    verbose=1
)

results = model.evaluate(test_data, test_labels)

print(results)
