import numpy
from Day19.vector import Vector

class Result:
    def __init__(self):
        self.beacons = set()
        # self.vectors = {}
        self.scanners = []
            
    def __str__(self):
        return 'Beacons no: ' + str(len(self.beacons)) + ' Scanners no: ' + str(len(self.scanners))
    
    def __repr__(self):
        return str(self)
    
    def addScanner(self, scanner, matrix, distance):
        scanner.rotateBeacons(matrix)
        scanner.updateBeaconsPosition(distance)
        scanner.calculatePartialVectors()
        scanner.distanceToZero = distance
        
        self.beacons.update(scanner.beacons)
        self.scanners.append(scanner)

        
