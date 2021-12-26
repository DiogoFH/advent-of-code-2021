class Segment:
    def __init__(self, start):
        self.start = start 
        self.end = None
        self.cubeList = set()

    def __str__(self):
        return str(self.start) + ', ' + str(self.end)
    
    def __repr__(self):
        return str(self)
