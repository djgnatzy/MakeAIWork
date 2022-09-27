
from re import S


class Car:
    def __init__(self, name, aMax, vMax):
        
        # v in m/s (km/h to m/s is: /3.6)
        # a in m/s/s
        
        
        self.name = name
        self.v = 0.0
        self.x = 0.0
        self.vMax = 0.0
        self.aMax = 0.0
        
    
    def move(self, dt):
 
        pass
    
        # a = self.F / self.m

        # dv = a * dt
        # self.v = self.v + dv

        # print("Velocity " + self.name + ": " + str(self.v))

        # dx = self.v * dt
        # self.x = self.x + dx

        # print("Position "  + self.name + " " + str(self.x))