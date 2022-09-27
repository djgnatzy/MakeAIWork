import tensorflow as tf
keras = tf.keras

import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=4, suppress=True)

filename = "C:/MakeAIWork/simulations/car/control_client/tensorflow_lidar _01_test.csv"

lidar_01_train = pd.read_csv(filename, header = 0, sep = ',')
# print(lidar_01_train)
# type(lidar_01_train)

# lidar_01_train.style

lidar_01_sensors = lidar_01_train.copy()
lidar_01__labels = lidar_01_sensors.pop('Steering Angle')

# print(lidar_01__labels)

lidar_01_sensors = np.array(lidar_01_sensors)

# print(lidar_01_sensors)

normalize = keras.layers.Normalization()
normalize.adapt(lidar_01_sensors)

norm_lidar_01_model = tf.keras.Sequential([
  normalize,
  keras.layers.Dense(64, activation = 'relu'),
  keras.layers.Dense(32, activation = 'relu'),
  keras.layers.Dense(1)
])

norm_lidar_01_model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'],
                            optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001))

norm_lidar_01_model.fit(lidar_01_sensors, lidar_01__labels, epochs = 50)