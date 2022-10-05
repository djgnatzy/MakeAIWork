import tensorflow as tf
keras = tf.keras

import pandas as pd
import numpy as np

# Make numpy values easier to read.
np.set_printoptions(precision=4, suppress=True)

filename = "C:/MakeAIWork/simulations/car/control_client/sonar.csv"

sonar_01_train = pd.read_csv(filename, header = 0, sep = ',')
# print(sonar_01_train)
# type(sonar_01_train)

# sonar_01_train.head()

sonar_01_sensors = sonar_01_train.copy()
sonar_01__labels = sonar_01_sensors.pop('Steering Angle')

# print(sonar_01__labels)

sonar_01_sensors = np.array(sonar_01_sensors)

# print(sonar_01_sensors)

normalize = keras.layers.Normalization()
normalize.adapt(sonar_01_sensors)

norm_sonar_01_model = tf.keras.Sequential([
  normalize,
  keras.layers.Dense(64, activation = 'relu'),
  keras.layers.Dense(64, activation = 'relu'),
  keras.layers.Dense(64),
  keras.layers.Dense(1)
])

norm_sonar_01_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                            optimizer = tf.keras.optimizers.Adam(learning_rate = 0.0001))

norm_sonar_01_model.fit(sonar_01_sensors, sonar_01__labels, epochs = 1000)