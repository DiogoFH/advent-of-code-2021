class Node:
    def __init__(self, name):
        self.name = name
        self.isSmall = name.islower()
        self.adjacencyList = []
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self)