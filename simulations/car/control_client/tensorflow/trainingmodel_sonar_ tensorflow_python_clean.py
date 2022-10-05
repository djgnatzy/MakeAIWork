import tensorflow as tf
keras = tf.keras
from keras import Model

import pandas as pd
import numpy as np

np.set_printoptions(precision=4, suppress=True)

filename = "../sonar_kevin.csv"

sonar_01_train = pd.read_csv(filename, sep = ',')

sonar_01_labels = sonar_01_train.iloc[:, [3]]
sonar_01_sensors = sonar_01_train.iloc[:,[0, 1, 2]]

sonar_01_sensors = np.array(sonar_01_sensors)

val_sonar_01_sensors = np.array(sonar_01_sensors [500:799])
val_sonar_01_labels = np.array(sonar_01_labels [500:799])

normalize = keras.layers.Normalization()
normalize.adapt(sonar_01_sensors)

norm_sonar_01_model = tf.keras.Sequential([
  normalize,
  keras.Input(shape = (3,)),
  keras.layers.Dense(16, activation = 'relu'), 
  keras.layers.Dense(16, activation = 'relu'),
  keras.layers.Dense(1)
])  

norm_sonar_01_model.compile(
                            loss = tf.keras.losses.MeanSquaredError(), 
                            metrics = ['accuracy', 'mae'], 
                            optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
                           )

norm_sonar_01_model.summary()

norm_sonar_01_model.fit(sonar_01_sensors, sonar_01_labels, epochs=500)

norm_sonar_01_model.evaluate(val_sonar_01_sensors, val_sonar_01_labels)

norm_sonar_01_model.predict(val_sonar_01_sensors)

norm_sonar_01_model.save('norm_sonar_01_model')