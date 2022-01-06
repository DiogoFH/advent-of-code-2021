class ALU:
    
    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
    
    def processInstructions(self, instructions, inp, z):
        self.z = z
        self.w = inp
        
        for instruction in instructions:
            inst, a, b = instruction.split(' ')
            if inst == 'add':
                self.add(a,b)
            elif inst == 'mul':
                self.mul(a,b)
            elif inst == 'div':
                self.div(a,b)
            elif inst == 'mod':
                self.mod(a,b)
            elif inst == 'eql':
                self.eql(a,b)
                
        return self.z
            
        
    def add(self, a, b):
        self.setVarValue(a, self.getValueFromVar(a) + self.getBValue(b))
    
    def mul(self, a, b):
        self.setVarValue(a, self.getValueFromVar(a) * self.getBValue(b))
    
    def div(self, a, b):
        self.setVarValue(a, self.getValueFromVar(a) // self.getBValue(b))
    
    def mod(self, a, b):
        self.setVarValue(a, self.getValueFromVar(a) % self.getBValue(b))
    
    def eql(self, a, b):
        if self.getValueFromVar(a) == self.getBValue(b):
            self.setVarValue(a, 1)
        else:
            self.setVarValue(a, 0)
        
    def getValueFromVar(self, var):
        if var == 'w':
            return self.w
        elif var == 'x':
            return self.x
        elif var == 'y':
            return self.y
        elif var == 'z':
            return self.z
    
    def isVar(self, var):
        if var in ('w', 'x', 'y', 'z'):
            return True
        else:
            return False
        
    def setVarValue(self, var, value):
        if var == 'w':
            self.w = value
        elif var == 'x':
            self.x = value
        elif var == 'y':
            self.y = value
        elif var == 'z':
            self.z = value
            
    def getBValue(self, b):
        if self.isVar(b):
            return self.getValueFromVar(b)
        else:
            return int(b)