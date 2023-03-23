import h5py
import pandas as pd
import numpy as np
import os
import tensorflow as tf

# https://www.tensorflow.org/tutorials/keras/save_and_load#hdf5_format

fp = os.path.dirname(__file__) + '/alien.h5'

with h5py.File(fp) as data_file:
    for k in data_file.keys():
        print(k) # root level object names - groups or datasets
        # print(type(data_file[k]))

    model_weights = data_file['model_weights']
    optimizer_weights = data_file['optimizer_weights']

    print('model_weights')
    for mk in model_weights:
        print(mk)
        print(type(model_weights[mk]))

    print('\n optimizer_weights')
    for mk in optimizer_weights:
        print(mk)
        print(type(optimizer_weights[mk]))


model = tf.keras.models.load_model(fp)
model.build(input_shape=[None, 32, 32, 3])
model.summary()

# conv2d_3_input [None, 32, 32, 3]

# test_input = np.random.random((1, 32, 32, 3))
# test_target = np.random.random((1, 32, 32, 3))

n_class = 3
n_features = 32
n_sample = 1000

X = np.random.randint(0, 10, (n_sample, n_features, n_features, n_class))
y = np.random.randint(0,n_class, n_sample)

model.fit(X, y, epochs=3)

prediction = model.predict(X)
print(prediction)

# SFRCe24wdF9zb
