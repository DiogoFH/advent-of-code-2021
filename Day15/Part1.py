#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

from Day15.node import Node

def solver():
    with open(__ficheiro, 'r') as file:
        riskMap = [[int(elem) for elem in line.strip()] for line in file.readlines()]
        
        lowestRisk = [[Node(y, x) for x,elem in enumerate(line)] for y,line in enumerate(riskMap)]
        endX = len(lowestRisk[0])-1
        endY = len(lowestRisk)-1
        
        unvisited = [node for line in lowestRisk for node in line]
        
        lowestRisk[0][0].risk = 0
        
        # print(riskMap)
        # print(lowestRisk)
        # print(unvisited)

        
        currentNode = lowestRisk[0][0]
        while currentNode is not None:
            for node in getNeighbours(currentNode, lowestRisk):
                newRisk = currentNode.risk + riskMap[node.x][node.y]
                if node.risk is None or node.risk > newRisk:
                    node.risk = newRisk
            # print(currentNode)
            unvisited.remove(currentNode)
            
            if lowestRisk[endX][endY].risk is not None:
                currentNode = None
            else:
                currentNode = sorted(unvisited, key=lambda node: (node.risk is None, node.risk))[0]
                
            
        
        print(lowestRisk[endX][endY].risk)
      
            
def getNeighbours(node, lowestRisk):
    x = node.x
    y = node.y
    neighbours = set()
    if x == 0:
        if y == 0:
            neighbours.add(lowestRisk[x+1][y])
            neighbours.add(lowestRisk[x][y+1])
        elif y == (len(lowestRisk)-1):
            neighbours.add(lowestRisk[x][y-1])
            neighbours.add(lowestRisk[x+1][y])
        else:
            neighbours.add(lowestRisk[x][y-1])
            neighbours.add(lowestRisk[x+1][y])
            neighbours.add(lowestRisk[x][y+1])
    elif x == (len(lowestRisk[0])-1):
        if y == 0:
            neighbours.add(lowestRisk[x-1][y])
            neighbours.add(lowestRisk[x][y+1])
        elif y == (len(lowestRisk)-1):
            neighbours.add(lowestRisk[x][y-1])
            neighbours.add(lowestRisk[x-1][y])
        else:
            neighbours.add(lowestRisk[x][y-1])
            neighbours.add(lowestRisk[x-1][y])
            neighbours.add(lowestRisk[x][y+1])
    else:
        if y == 0:
            neighbours.add(lowestRisk[x-1][y])
            neighbours.add(lowestRisk[x+1][y])
            neighbours.add(lowestRisk[x][y+1])
        elif y == (len(lowestRisk)-1):
            neighbours.add(lowestRisk[x-1][y])
            neighbours.add(lowestRisk[x+1][y])
            neighbours.add(lowestRisk[x][y-1])
        else:
            neighbours.add(lowestRisk[x+1][y])
            neighbours.add(lowestRisk[x-1][y])
            neighbours.add(lowestRisk[x][y+1])
            neighbours.add(lowestRisk[x][y-1])
    return neighbours
        
            

if __name__ == "__main__":
    solver()