### Plan
# class object that holds a 2d array of uplift values
# functions for:
# generate with see and params

import opensimplex as simp
import numpy as np

class upliftMap:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.seed = 0
        self.map = np.empty((self.height, self.width))
    
    def setseed(self, seed):
            self.seed = seed
            simp.seed(self.seed)

    def generate(self, wid, hih):
        self.map = np.zeros((wid,hih))

        self.map = simp.noise2array(wid, hih)

        
    
#---------------  
def main(): #test function
    lift = upliftMap()
    lift.setseed(524902)
    lift.generate(10,10)
    print(lift.map)

if __name__=="__main__":
    main()
