#__ficheiro = 'sampleInput.txt'
#__ficheiro = 'sampleInput2.txt'
#__ficheiro = 'sampleInput3.txt'
__ficheiro = 'input.txt'

from Day12.node import Node

def solver():
    nodeList = readInput()
    
    #printNodeList(nodeList)
    
    paths = explore(nodeList['start'], [])
    print(paths)
    
def printNodeList(nodeList):
    for n in list(nodeList.values()):
        print(n.name, n.adjacencyList)
        
def readInput():
    nodeList = {}
    with open(__ficheiro, 'r') as file:
        for line in file:
            nodes = line.strip().split('-')
            if not nodes[0] in nodeList:
                nodeList[nodes[0]] = Node(nodes[0])
            if not nodes[1] in nodeList:
                nodeList[nodes[1]] = Node(nodes[1])
            
            if nodes[0] != 'end' and nodes[1] != 'start':
                nodeList[nodes[0]].adjacencyList.append(nodeList[nodes[1]])
            if nodes[1] != 'end' and nodes[0] != 'start':
                nodeList[nodes[1]].adjacencyList.append(nodeList[nodes[0]])
                
    return nodeList

def explore(node, currentPath):
    currentPath.append(node)
    if node.name == 'end':
        #printPath(currentPath)
        currentPath.pop()
        return 1
    paths = 0
    for a in node.adjacencyList:
        if a.isSmall and isInPath(a, currentPath):
            continue
        paths += explore(a, currentPath)
    currentPath.pop()
    return paths
    
def isInPath(a, currentPath):
    for node in currentPath:
        if node == a:
            return True
    return False

def printPath(path):
    for n in path:
        print(n.name, end='->')
    print()

if __name__ == "__main__":
    solver()