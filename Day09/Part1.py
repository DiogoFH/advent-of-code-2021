#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        heightmap = [[elem for elem in line.strip()] for line in file.readlines()]
        sizeX = len(heightmap[0])
        sizeY = len(heightmap) 
        
        riskSum = 0
        
        for y in range(sizeY):
            for x in range(sizeX):
                if      (( y == 0 or heightmap[y][x] < heightmap[y-1][x])
                    and ( y == sizeY-1 or heightmap[y][x] < heightmap[y+1][x])
                    and ( x == 0 or heightmap[y][x] < heightmap[y][x-1])
                    and ( x == sizeX-1 or heightmap[y][x] < heightmap[y][x+1])):
                        #print(x,y)
                        #print(heightmap[y][x])
                        riskSum += int(heightmap[y][x]) + 1
            
        print(riskSum)
    
if __name__ == "__main__":
    solver()