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



lidar_01_sensors = np.array(lidar_01_sensors)

# print(lidar_01_sensors)

normalize = keras.layers.Normalization()
normalize.adapt(lidar_01_sensors)

# Kijken of het mogelijk is om het startpunt vast te zetten, nu variabel.

norm_lidar_01_model = tf.keras.Sequential([
  normalize,
  keras.layers.Dense(64, activation = 'elu'),
  keras.layers.Dense(64, activation = 'elu'),
  keras.layers.Dense(64)
])

norm_lidar_01_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                            optimizer = tf.keras.optimizers.Adam(learning_rate=0.00001)) 

history = norm_lidar_01_model.fit(lidar_01_sensors, lidar_01__labels, epochs = 200)

# norm_lidar_01_model.summary()

# # history.history

# print("Evaluate")
# result = norm_lidar_01_model.evaluate(norm_lidar_01_model)