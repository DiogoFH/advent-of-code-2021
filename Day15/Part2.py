#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

from Day15.node import Node

def solver():
    with open(__ficheiro, 'r') as file:
        lines = file.readlines()
        riskMap = [[int(elem)+i+j for i in range(5) for elem in line.strip()] for j in range(5) for line in lines]
        
        for x,line in enumerate(riskMap):
            for y,i in enumerate(line):
                if i > 9:
                    riskMap[x][y] = i-9
        
        lowestRisk = [[Node(x, y) for y,elem in enumerate(line)] for x,line in enumerate(riskMap)]
        endX = len(lowestRisk[0])-1
        endY = len(lowestRisk)-1
        
        # unvisited = [node for line in lowestRisk for node in line]
        unvisited = [lowestRisk[0][0]]
        
        lowestRisk[0][0].risk = 0
        
        # for a in riskMap:
        #     print(a)
        # # print(riskMap[0])
        # print(lowestRisk)
        # print(unvisited)

        
        currentNode = lowestRisk[0][0]
        while currentNode is not None:
            for node in getNeighbours(currentNode, lowestRisk):
                newRisk = currentNode.risk + riskMap[node.x][node.y]
                if node.risk is None:
                    node.risk = newRisk
                    unvisited.append(node) 
                elif node.risk > newRisk:
                    node.risk = newRisk
                    
            # print(currentNode)
            # print(len(unvisited))
            unvisited.remove(currentNode)
        
            if lowestRisk[endX][endY].risk is not None:
                currentNode = None
            else:
                currentNode = sorted(unvisited, key=lambda node: node.risk)[0]
        
        
        
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