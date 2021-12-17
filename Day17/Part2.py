import math

#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    minTargetX, maxTargetX, minTargetY, maxTargetY = parseInput()
    
    # print(minTargetX)
    # print(maxTargetX)
    # print(minTargetY)
    # print(maxTargetY)
    
    # list of x values that reach target and corresponding steps
    lista = [(x,[step for step in range(1, x+1) if (x+(x-step+1))/2 * step >= minTargetX and (x+(x-step+1))/2 * step <= maxTargetX]) for x in range(1,maxTargetX+1) ]
    lista = list(filter(lambda x: x[1] != [], lista))
    
    count = 0
    for x, steps in lista:
        ySet = set()
        for step in steps:
            ySet = set.union(ySet,getYList(step, minTargetY, maxTargetY))
            if x == step :
                for infinityStep in range(step+1, 100000):      #Fuck it x2!
                    ySet = set.union(ySet,getYList(infinityStep, minTargetY, maxTargetY))
        count += len(ySet)
        
    print(count)
            
def getYList(step, minTargetY, maxTargetY):
    # print(step, minTargetY, maxTargetY)
    minVInit = (minTargetY - 0.5 * step + 0.5 * step**2)/step
    maxVInit = (maxTargetY - 0.5 * step + 0.5 * step**2)/step
    if math.ceil(minVInit) <= math.floor(maxVInit):
        return range( math.ceil(minVInit), math.floor(maxVInit)+1)
    else:
        return []

      
def parseInput():
    with open(__ficheiro, 'r') as file:
        targetArea = file.read()
        minXStart = targetArea.index('=')+1
        minXEnd =  targetArea.index('..')
        maxXStart = targetArea.index('..')+2
        maxXEnd = targetArea.index(',')

        minYStart = targetArea.index('=', maxXEnd)+1
        minYEnd =  targetArea.index('..', maxXEnd)
        maxYStart = targetArea.index('..', maxXEnd)+2
        
        return int(targetArea[minXStart:minXEnd]), int(targetArea[maxXStart:maxXEnd]), int(targetArea[minYStart:minYEnd]), int(targetArea[maxYStart:])

if __name__ == "__main__":
    solver()