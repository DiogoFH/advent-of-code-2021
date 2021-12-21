#__ficheiro = 'sampleInput.txt'
#__ficheiro = 'sampleInput2.txt'
__ficheiro = 'input.txt'

import ast
import numpy
from Day19.scanner import Scanner
from Day19.vector import Vector
from Day19.result import Result

rotMatrices = [
    numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
    numpy.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
    numpy.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
    numpy.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
    numpy.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
    numpy.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    numpy.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),
    numpy.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
    numpy.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
    numpy.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),
    numpy.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),
    numpy.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),
    numpy.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]]),
    numpy.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
    numpy.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
    numpy.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
    numpy.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    numpy.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),
    numpy.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
    numpy.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]]),
    numpy.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),
    numpy.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),
    numpy.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
    ]

def solver():
    scanners = parseInput()

    for scanner in scanners[1:]:
        scanner.calculateAllVectors()
    
    resultado = Result()
    resultado.addScanner(scanners[0], rotMatrices[0], (0,0,0))
    scanners.remove(scanners[0])
    
    print(resultado)
    
    while scanners != []:
        # print('while ', len(scanners))
        for scanner in scanners:
            # print('for ', scanner.name)
            for rotMatrix in rotMatrices:
                rotatedVectors = []
                for beaconVector in scanner.vectors:
                    rotatedVectors.append(Vector(beaconVector.beacon1, beaconVector.beacon2, numpy.dot(rotMatrix,beaconVector.v)))
                    
                for resScanner in resultado.scanners:    
                    equalSample = checkCommonVectors(rotatedVectors, resScanner.vectorsDict)
                    if equalSample is not None:
                        # print('match')
                        distance = calculateDistance(equalSample, rotMatrix)
                        resultado.addScanner(scanner, rotMatrix, distance)
                        print(resultado)
                        scanners.remove(scanner)
                        break
                
    maxDistance = 0    
    for scanner1 in resultado.scanners:
        for scanner2 in resultado.scanners:
            if scanner1 != scanner2:
                newDistance = abs(scanner2.distanceToZero[0]-scanner1.distanceToZero[0]) + abs(scanner2.distanceToZero[1]-scanner1.distanceToZero[1]) + abs(scanner2.distanceToZero[2]-scanner1.distanceToZero[2])
                if newDistance > maxDistance:
                    maxDistance = newDistance
    print(maxDistance)

def parseInput():
    with open(__ficheiro, 'r') as file:
        scanners = []
        
        for line in file:
            if line[0:3] == '---':
                scanner = Scanner(line[4:-5])
                scanners.append(scanner)
            elif line == '\n':
                pass
            else:
                scanner.beacons.append(ast.literal_eval(line.strip()))
    return scanners

def checkCommonVectors(list1, resultVectors):
    commonBeacons = set()
    for v1 in list1:
        if v1.v[0] in resultVectors:
            for v2 in resultVectors[v1.v[0]]:
                if numpy.array_equal(v1.v, v2.v):
                    commonBeacons.add(v1.beacon1)
                    commonBeacons.add(v1.beacon2)
                    if len(commonBeacons) >= 12:
                        return v1, v2
    return None

def calculateDistance(equalSample, rotMatrix):
    rotated = numpy.dot(rotMatrix,equalSample[0].beacon1)
    return equalSample[1].beacon1[0] - rotated[0], equalSample[1].beacon1[1] - rotated[1], equalSample[1].beacon1[2] - rotated[2],   
    
        
if __name__ == "__main__":
    solver()
   