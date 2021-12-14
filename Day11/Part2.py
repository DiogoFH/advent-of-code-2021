#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

from Day11.octopus import Octopus

def solver():
    grid = []
    with open(__ficheiro, 'r') as file:
        for y,line in enumerate(file):
            gridLine = []
            for x,c in enumerate(line.strip()):
                gridLine.append(Octopus(x,y,int(c)))
            grid.append(gridLine)
    
    flashes = 0
    step = 0
    while flashes != 100:
        step += 1
    #for step in range(100):
        increasePowerLevel(grid)
        newFlashes = flash(grid)
        flashes = newFlashes
        while newFlashes > 0:
            newFlashes = flash(grid)
            flashes += newFlashes
        resetPowerLevelFlashed(grid)
        if flashes == 100:
            break
    
    print(step)
    printGrid(grid)
    print(flashes)
       
def printGrid(grid):
    for y in range(10):
        for x in range(10):
            print(grid[y][x].energyLevel, end='')
        print()
        
def increasePowerLevel(grid):
    for line in grid:
            for o in line:
                o.energyLevel += 1
                
def increasePowerLevelNeighbours(grid, x, y):
    for o in grid[y][x].neighbours:
        grid[o[1]][o[0]].energyLevel += 1
    
def flash(grid):
    flashes = 0
    for line in grid:
        for o in line:
            if o.energyLevel > 9 and not o.hasFlashed:
                flashes += 1
                o.hasFlashed = True
                increasePowerLevelNeighbours(grid, o.x, o.y)
    return flashes

def resetPowerLevelFlashed(grid):
    for line in grid:
        for o in line:
            o.hasFlashed = False
            if o.energyLevel > 9:
                o.energyLevel = 0

if __name__ == "__main__":
    solver()