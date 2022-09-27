import time as tm
from car import Car


class World:
    
    def __init__(self):
        
        self.t = 0.0
        self.dt = 0.1 
        
        self.running = True
        
        # 150 km/h = 41.66667 m/s
        # 220 km/h = 61.11111 m/s
        
        self.carT = Car("Tesla", 10, 150.0)
        self.carB = Car("BMW", 5, 220.0)
        
        
        
    def bang(self):
         
        while self.running:
             
            self.t += self.dt

            self.carT.move(self.dt)
            self.carB.move(self.dt)
            
            print("\nTime:            ", self.t)
            
            if self.carT.x > 100.0:
                
                print("\nTesla is victorious!\n")
                
                self.running = False
                
            if self.carB.x > 100.0:
                
                print("\nBMW is victorious!\n")
                
                self.running = False
                 
        
                tm.sleep(self.dt)
            