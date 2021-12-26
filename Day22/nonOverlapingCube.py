class NonOverlapingCube:
    def __init__(self, xInit, xEnd, yInit, yEnd, zInit, zEnd, on):
        self.xInit = xInit 
        self.xEnd = xEnd 
        self.yInit = yInit 
        self.yEnd = yEnd 
        self.zInit = zInit 
        self.zEnd = zEnd 
        self.on = on 
        
    def __str__(self):
        return str(self.xInit) + ', ' + str(self.xEnd) + ', ' + str(self.yInit) + ', ' + str(self.yEnd) + ', ' + str(self.zInit) + ', ' + str(self.zEnd) + ', ' + str(self.on)  
    
    def __repr__(self):
        return str(self)
