import time as tm
from car import Car


class World:
    
    def __init__(self):
        
        self.t = 0.0
        self.dt = 0.1 
        
        self.running = True
        
        self.carT = Car("Tesla", 1200.0, 300.0)
        self.carB = Car("BMW", 1600.0, 500.0)
        
        
        
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
            