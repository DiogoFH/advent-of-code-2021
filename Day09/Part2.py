#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

heightmap = []
sizeX = 0
sizeY = 0

def solver():
    with open(__ficheiro, 'r') as file:
        global heightmap, sizeX, sizeY
        
        heightmap = [[elem for elem in line.strip()] for line in file.readlines()]
        sizeX = len(heightmap[0])
        sizeY = len(heightmap) 

        basinSizes = []
        
        for y in range(sizeY):
            for x in range(sizeX):
                if      (( y == 0 or heightmap[y][x] < heightmap[y-1][x])
                    and ( y == sizeY-1 or heightmap[y][x] < heightmap[y+1][x])
                    and ( x == 0 or heightmap[y][x] < heightmap[y][x-1])
                    and ( x == sizeX-1 or heightmap[y][x] < heightmap[y][x+1])):
                        basinSizes.append(calculateBasinSize(y, x))
            
        print(basinSizes)
        sortedBasinSizes = sorted(basinSizes, reverse=True) 
        print(sortedBasinSizes)
        print(sortedBasinSizes[0] * sortedBasinSizes[1] * sortedBasinSizes[2])
    
def calculateBasinSize(y, x):
    basin = {(y,x)}
    newMembers = set()
    
    for (y1,x1) in vizinhos(y, x):
        if heightmap[y1][x1] != '9':
            newMembers.add((y1,x1))
    
    newMembers = newMembers.difference(basin)
    
    while len(newMembers) > 0:
        basin = basin.union(newMembers)
        aux = newMembers
        newMembers = set()
        for (y2,x2) in aux:
            for (y1,x1) in vizinhos(y2, x2): 
                if heightmap[y1][x1] != '9':
                    newMembers.add((y1,x1))
        newMembers = newMembers.difference(basin)
            
    
    #print(basin)
    return len(basin)

def vizinhos(y, x):
    vizinhos = set()
    if y == 0:
        if x == 0:
            vizinhos.add((y,x+1))
            vizinhos.add((y+1,x))
        elif x == sizeX-1:
            vizinhos.add((y,x-1))
            vizinhos.add((y+1,x))
        else:
            vizinhos.add((y,x-1))
            vizinhos.add((y,x+1))
            vizinhos.add((y+1,x))
    elif y == sizeY-1:
        if x == 0:
            vizinhos.add((y,x+1))
            vizinhos.add((y-1,x))
        elif x == sizeX-1:
            vizinhos.add((y,x-1))
            vizinhos.add((y-1,x))
        else:
            vizinhos.add((y,x-1))
            vizinhos.add((y,x+1))
            vizinhos.add((y-1,x))
    else:
        if x == 0:
            vizinhos.add((y,x+1))
            vizinhos.add((y-1,x))
            vizinhos.add((y+1,x))
        elif x == sizeX-1:
            vizinhos.add((y,x-1))
            vizinhos.add((y-1,x))
            vizinhos.add((y+1,x))
        else:
            vizinhos.add((y,x-1))
            vizinhos.add((y,x+1))
            vizinhos.add((y-1,x))
            vizinhos.add((y+1,x))
        
    # print(y, x)
    # print(vizinhos)
    return vizinhos
    
if __name__ == "__main__":
    solver()