import tensorflow as tf
keras = tf.keras
from keras import Model
import numpy as np

import time as tm
import sys as ss
import os
import socket as sc

ss.path += [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters as pm

import pickle
import sklearn as sk
from sklearn.neural_network import MLPClassifier

mpl = pickle.load('C:/MakeAIWork/simulations/car/control_client/scikitlearn/pickle_model.pkl')

sample = [pm.finity for entryindex in range (pm.sonarInputDim)]
steeringAngle = mpl.predict(np.array(sample))

print(mpl)