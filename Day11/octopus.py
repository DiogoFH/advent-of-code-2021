class Octopus:
    def __init__(self, x, y, energyLevel):
        self.x = x
        self.y = y
        self.energyLevel = energyLevel
        self.neighbours = []
        self._initializeNeighbours(x, y)
        self.hasFlashed = False
        
    def _initializeNeighbours(self, x, y):
        if x == 0:
            if y == 0:
                #top left corner
                self.neighbours.append((1,0))
                self.neighbours.append((0,1))
                self.neighbours.append((1,1))
            elif y == 9:
                #bottom left corner
                self.neighbours.append((0,8))
                self.neighbours.append((1,8))
                self.neighbours.append((1,9))
            else:
                #left border
                self.neighbours.append((0,y-1))
                self.neighbours.append((1,y-1))
                self.neighbours.append((1,y))
                self.neighbours.append((0,y+1))
                self.neighbours.append((1,y+1))
        elif x == 9:
            if y == 0:
                #top right corner
                self.neighbours.append((8,0))
                self.neighbours.append((8,1))
                self.neighbours.append((9,1))
            elif y == 9:
                #bottom right corner
                self.neighbours.append((9,8))
                self.neighbours.append((8,8))
                self.neighbours.append((8,9))
            else:
                #right border
                self.neighbours.append((9,y-1))
                self.neighbours.append((8,y-1))
                self.neighbours.append((8,y))
                self.neighbours.append((9,y+1))
                self.neighbours.append((8,y+1))
        else:
            if y == 0:
                #top row (minus corners)
                self.neighbours.append((x-1,0))
                self.neighbours.append((x+1,0))
                self.neighbours.append((x-1,1))
                self.neighbours.append((x,1))
                self.neighbours.append((x+1,1))
            elif y == 9:
                #bottom row (minus corners)
                self.neighbours.append((x-1,8))
                self.neighbours.append((x,8))
                self.neighbours.append((x+1,8))
                self.neighbours.append((x-1,9))
                self.neighbours.append((x+1,9))
            else:
                self.neighbours.append((x-1,y-1))
                self.neighbours.append((x-1,y))
                self.neighbours.append((x-1,y+1))
                self.neighbours.append((x,y-1))
                self.neighbours.append((x,y+1))
                self.neighbours.append((x+1,y-1))
                self.neighbours.append((x+1,y))
                self.neighbours.append((x+1,y+1))

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        