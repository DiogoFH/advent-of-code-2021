import numpy

from Day19.vector import Vector

class Scanner:
    def __init__(self, name):
        self.name = name 
        self.beacons = []
        self.vectors = []
        self.vectorsDict = {}
        self.distanceToZero = ()
        
    def __str__(self):
        return str(self.name) + ' Distance to zero: ' + str(self.distanceToZero)
    
    def __repr__(self):
        return str(self)
    
    
    def calculatePartialVectors(self):
        self.vectorsDict = {}
        for i in range(len(self.beacons)):
            for j in range(i+1, len(self.beacons)):
                vector = Vector(self.beacons[j], self.beacons[i])
                if vector.v[0] in self.vectorsDict:
                    self.vectorsDict[vector.v[0]].append(vector)
                else:
                    self.vectorsDict[vector.v[0]] = [vector]
    
    def calculateAllVectors(self):
        self.vectors = []
        for i in range(len(self.beacons)):
            for j in range(len(self.beacons)):
                if i != j:
                    self.vectors.append(Vector(self.beacons[j], self.beacons[i]))
                    
                    
    def rotateBeacons(self, matrix):
        # testar se dá para fazer inplace?
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append(numpy.dot(matrix,beacon))
        self.beacons = newBeacons
                    
    def updateBeaconsPosition(self, distance):
        # testar se dá para fazer inplace?
        newBeacons = []
        for beacon in self.beacons:
            newBeacons.append((beacon[0] + distance[0], beacon[1] + distance[1], beacon[2] + distance[2]))
        self.beacons = newBeacons
        

