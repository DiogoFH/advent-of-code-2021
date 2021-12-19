import math
from pickle import TRUE

class SnailfishNumber:
    def __init__(self, lista= None, parent=None):
        if isinstance(lista, list):
            self.left = SnailfishNumber(lista[0], self)
            self.right = SnailfishNumber(lista[1], self)
            self.parent = parent
            self.isLeaf = False
        else:
            self.isLeaf = True
            self.value = lista
            self.parent = parent
        
    def __str__(self):
        if self.isLeaf:
            return str(self.value)
        else:
            return '[' + str(self.left) + ',' + str(self.right) + ']'
    
    def __repr__(self):
        return str(self)
    
    def __add__(self, other):
        newNumber = SnailfishNumber()
        newNumber.left = self
        newNumber.right = other
        newNumber.isLeaf = False
        self.parent = newNumber
        other.parent = newNumber
        newNumber.reduce()
        return newNumber
    
    def magnitude(self):
        if self.isLeaf:
            return self.value
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()
    
    def reduce(self):
        reduced = TRUE
        while reduced:
            if not self.searchExplode(0):
                reduced = self.searchSplit()
        
    def searchExplode(self, currenteDepth):
        if self.isLeaf:
            return False
        elif currenteDepth == 4:
            self.explode()
            return True
        else:
            if self.left.searchExplode(currenteDepth+1):
                return True
            elif self.right.searchExplode(currenteDepth+1):
                return True
            else:
                return False
        
    def searchSplit(self):
        if self.isLeaf:
            if self.value > 9:
                self.split()
                return True
            else:
                return False
        else:
            if self.left.searchSplit():
                return True
            elif self.right.searchSplit():
                return True
            else:
                return False

    def split(self):
        # print('split', self)
        self.left = SnailfishNumber(math.floor(self.value/2), self)
        self.right = SnailfishNumber(math.ceil(self.value/2), self)
        self.isLeaf = False
        

    def explode(self):
        # print('explode', self)
        leftValue = self.searchLeftValue()
        rightValue = self.searchRightValue()
        if leftValue != None:
            leftValue.value += self.left.value
        if rightValue != None:
            rightValue.value += self.right.value
            
        self.value = 0
        self.isLeaf = True
        self.left = self.right = None
                
    def searchLeftValue(self):
        currentNode = self
        while currentNode.parent != None:
            if currentNode.parent.right == currentNode:
                leftValue = currentNode.parent.left
                while not leftValue.isLeaf:
                    leftValue = leftValue.right
                return leftValue
            else:
                currentNode = currentNode.parent
        return None
            
    def searchRightValue(self):
        currentNode = self
        while currentNode.parent != None:
            if currentNode.parent.left == currentNode:
                rightValue = currentNode.parent.right
                while not rightValue.isLeaf:
                    rightValue = rightValue.left
                return rightValue
            else:
                currentNode = currentNode.parent
        return None
    
    
    
    