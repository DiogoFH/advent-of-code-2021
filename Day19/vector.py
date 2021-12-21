import numpy

class Vector:
    def __init__(self, beacon1=None, beacon2=None, v=None):
        self.beacon1 = beacon1
        self.beacon2 = beacon2
        if v is not None:
            self.v = v
        else:
            # print(self.beacon1, self.beacon2)
            self.v = numpy.array([self.beacon2[0] - self.beacon1[0],
                                  self.beacon2[1] - self.beacon1[1],
                                  self.beacon2[2] - self.beacon1[2]])
            
        
    def __str__(self):
        return 'Beacon1: ' + str(self.beacon1) + '\nBeacon2: ' + str(self.beacon2) + '\nVector: ' + str(self.v) + '\n'
    
    def __repr__(self):
        return str(self)
    
