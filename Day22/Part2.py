#__ficheiro = 'sampleInput3.txt'
#__ficheiro = 'sampleInput4.txt'
#__ficheiro = 'sampleInput5.txt'
__ficheiro = 'input.txt'

from Day22.cube import Cube
from Day22.segment import Segment
from Day22.nonOverlapingCube import NonOverlapingCube

def solver():
    cubeList = parseInput()
    print('parsed input: ', len(cubeList))
    xSegmentList = generateSegmentList(cubeList, lambda cube : cube.xInit, lambda cube : cube.xEnd)
    print('generateSegmentListX: ', len(xSegmentList))
    ySegmentList = generateSegmentList(cubeList, lambda cube : cube.yInit, lambda cube : cube.yEnd)
    print('generateSegmentListY: ', len(ySegmentList))
    zSegmentList = generateSegmentList(cubeList, lambda cube : cube.zInit, lambda cube : cube.zEnd)
    print('generateSegmentListZ: ', len(zSegmentList))
    
    generateNonOverlapingCube(xSegmentList, ySegmentList, zSegmentList)
    # nonOverlapingCubeList = generateNonOverlapingCube(xSegmentList, ySegmentList, zSegmentList)
    # print('generateNonOverlapingCube: ', len(nonOverlapingCubeList))
    #
    # print('count')
    # count = 0
    # for nonOverlapingCube in nonOverlapingCubeList:
    #     count += (nonOverlapingCube.xEnd - nonOverlapingCube.xInit + 1) * (nonOverlapingCube.yEnd - nonOverlapingCube.yInit + 1) * (nonOverlapingCube.zEnd - nonOverlapingCube.zInit + 1)
    #
    # print(count) 

def generateNonOverlapingCube(xSegmentSet, ySegmentSet, zSegmentSet):
    count = 0
    # nonOverlapingCubeList = []
    for xSegment in xSegmentSet:
        for ySegment in ySegmentSet:
            for zSegment in zSegmentSet:
                unionCubes = xSegment.cubeList & ySegment.cubeList & zSegment.cubeList 
                if len(unionCubes) != 0: 
                    if sorted(unionCubes, key=lambda cube : cube.order, reverse=True)[0].on:
                        nonOverlapingCube = NonOverlapingCube(xSegment.start, xSegment.end, ySegment.start, ySegment.end, zSegment.start, zSegment.end, True)
                        count += (nonOverlapingCube.xEnd - nonOverlapingCube.xInit) * (nonOverlapingCube.yEnd - nonOverlapingCube.yInit) * (nonOverlapingCube.zEnd - nonOverlapingCube.zInit)
    print(count)
    
def generateSegmentList(cubeList, initFunc, endFunc):
    pointList = [(initFunc(cube), True, cube) for cube in cubeList] + [(endFunc(cube)+1, False, cube) for cube in cubeList]
    
    pointList.sort(key=lambda point : point[0])
    
    segmentList = []
    currentCubes = []
    
    currentSegment = Segment(pointList[0][0])
    currentCubes.append(pointList[0][2])
    currentSegment.cubeList.update(currentCubes)
    
    for point in pointList[1:-1]:
        if point[1]:
            currentCubes.append(point[2])
        else:    
            currentCubes.remove(point[2])
        
        currentSegment.end = point[0]
        segmentList.append(currentSegment)
        currentSegment = Segment(point[0])
        
        currentSegment.cubeList.update(currentCubes)
        
    currentSegment.end = pointList[-1][0]
    segmentList.append(currentSegment)     
    
    return segmentList
        
def parseInput():
    cubeList = []
    with open(__ficheiro, 'r') as file:
        order = 0
        for line in file:
            on = line[0:2] == 'on'
            
            line = line[line.index('x=')+2:]
            xInit = int(line[:line.index('..')])
            xEnd = int(line[line.index('..')+2:line.index(',')])
            
            line = line[line.index('y=')+2:]
            yInit = int(line[:line.index('..')])
            yEnd = int(line[line.index('..')+2:line.index(',')])
            
            line = line[line.index('z=')+2:]
            zInit = int(line[:line.index('..')])
            zEnd = int(line[line.index('..')+2:].strip())
            cubeList.append(Cube(xInit, xEnd, yInit, yEnd, zInit, zEnd, order, on))
            
            order += 1
            
    return cubeList

if __name__ == "__main__":
    solver()
    
    

