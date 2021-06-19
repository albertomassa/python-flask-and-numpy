
import numpy as np

class VectorsDTO():

    def __init__(self, v1=None, v2=None, m1=None, m2=None):
        self.v1 = v1
        self.v2 = v2
        self.m1 = m1
        self.m2 = m2

    def getV1Vector(self):
        return np.fromstring(self.v1, dtype=float, sep=' ')
    
    def getV2Vector(self): 
        return np.fromstring(self.v2, dtype=float, sep=' ')

    def getM1Matrix(self):
        return np.matrix(self.m1)
    
    def getM2Matrix(self):
        return np.matrix(self.m2)