#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    region = parseInput()
    print(region)
    moved = True
    moveCount = 0
    while moved:
        moved, region = step(region)
        moveCount += 1
    
    print(region)
    print(moveCount)

def step(region):
    movedEast, region = moveEast(region)
    movedSouth, region = moveSouth(region)
    return movedEast or movedSouth, region
    
def moveEast(region):
    moved = False
    newRegion = [['.' for j in region[0]] for j in region]
    for l, line in enumerate(region):
        for c, column in enumerate(line):
            if region[l][c] == '>':
                if region[l][(c+1)%len(line)] == '.':
                    newRegion[l][(c+1)%len(line)] = '>'
                    moved = True
                else:
                    newRegion[l][c] = '>'
            elif region[l][c] == 'v':
                newRegion[l][c] = 'v'
    return moved, newRegion

def moveSouth(region):
    moved = False
    newRegion = [['.' for j in region[0]] for j in region]
    for l, line in enumerate(region):
        for c, column in enumerate(line):
            if region[l][c] == 'v':
                if region[(l+1)%len(region)][c] == '.':
                    newRegion[(l+1)%len(region)][c] = 'v'
                    moved = True
                else:
                    newRegion[l][c] = 'v'
            elif region[l][c] == '>':
                newRegion[l][c] = '>'
    return moved, newRegion
    
def parseInput():
    region = []
    with open(__ficheiro, 'r') as file:
        for line in file:
            region.append(line.strip())
    return region
    
if __name__ == "__main__":
    solver()
    
    

