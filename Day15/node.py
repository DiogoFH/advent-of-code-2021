class Node:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.risk = None
        
    def __str__(self):
        return str(self.x) + ',' + str(self.y) + ',' + str(self.risk) 
    
    def __repr__(self):
        return str(self)