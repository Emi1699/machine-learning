import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# keep whatever there is in the first argument, and reshape the second arg (basically, flatten the images
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0

# Sequential API  (Very convenient, not very flexible)
model = keras.Sequential(
    [
        keras.Input(shape=(28*28)),
        layers.Dense(512, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(10),
    ]
)

print(model.summary())

import sys
sys.exit()

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=['accuracy'],
)

model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=True)
model.evaluate(x_test, y_test, batch_size=32, verbose=True)