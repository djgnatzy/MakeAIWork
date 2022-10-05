#!/usr/bin/env python

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

loadSonarmodel = r'../control_client/tensorflow/norm_sonar_01_model'

class DrivingAgent:
    
    def __init__(self): # + **kwargs
        # self.name = kwargs['name']
        # print(self.name )   
        self.model = None
        self.steeringAngle = 0  

        with sc.socket (*sw.socketType) as self.clientSocket:
            self.clientSocket.connect (sw.address)
            self.socketWrapper = sw.SocketWrapper (self.clientSocket)
            self.halfApertureAngle = False

            while True:
                self.input ()
                self.sweep ()
                self.output()
                tm.sleep (0.02)
                
    def input (self):
        sensors = self.socketWrapper.recv()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
        else:
            self.sonarDistances = sensors ['sonarDistances']

    def lidarSweep (self):
        nearestObstacleDistance = pm.finity
        nearestObstacleAngle = 0
        
        nextObstacleDistance = pm.finity
        nextObstacleAngle = 0

#         for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
#             lidarDistance = self.lidarDistances [lidarAngle]
            
#             if lidarDistance < nearestObstacleDistance:
#                 nextObstacleDistance =  nearestObstacleDistance
#                 nextObstacleAngle = nearestObstacleAngle
                
#                 nearestObstacleDistance = lidarDistance 
#                 nearestObstacleAngle = lidarAngle

#             elif lidarDistance < nextObstacleDistance:
#                 nextObstacleDistance = lidarDistance
#                 nextObstacleAngle = lidarAngle
           
#         targetObstacleDistance = (nearestObstacleDistance + nextObstacleDistance) / 2

#         self.steeringAngle = (nearestObstacleAngle + nextObstacleAngle) / 2
#         self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sonarSweep (self):
        steeringAngleModel = self.model.predict(np.array(self.sonar_01_sensors))
        self.steeringAngle = float(steeringAngleModel [0][0])
        
        # obstacleDistances = [pm.finity for sectorIndex in range (3)]
        # obstacleAngles = [0 for sectorIndex in range (3)]
        
#         for sectorIndex in (-1, 0, 1):
#             sonarDistance = self.sonarDistances [sectorIndex]
#             sonarAngle = 2 * self.halfMiddleApertureAngle * sectorIndex
            
#             if sonarDistance < obstacleDistances [sectorIndex]:
#                 obstacleDistances [sectorIndex] = sonarDistance
#                 obstacleAngles [sectorIndex] = sonarAngle

#         if obstacleDistances [-1] > obstacleDistances [0]:
#             leftIndex = -1
#         else:
#             leftIndex = 0
           
#         if obstacleDistances [1] > obstacleDistances [0]:
#             rightIndex = 1
#         else:
#             rightIndex = 0
           
#         self.steeringAngle = (obstacleAngles [leftIndex] + obstacleAngles [rightIndex]) / 2
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)

#     def main():  
#         agent = DrivingAgent(name="Ashok Leyland Limited")
#         print("The agent is driving")
            
# if __name__ == "__main__":
#         main()
                
    
DrivingAgent()  # .main