#__ficheiro = 'sampleInput.txt'
#__ficheiro = 'sampleInput2.txt'
__ficheiro = 'input.txt'

def solver():
    cube = [[[False for i in range(101)] for j in range(101)] for k in range(101)]
    midPoint = 50
    with open(__ficheiro, 'r') as file:
        for line in file:
            # print(line.strip())
            
            on = line[0:2] == 'on'
            # print(on)
            
            line = line[line.index('x=')+2:]
            xInit = int(line[:line.index('..')])
            xEnd = int(line[line.index('..')+2:line.index(',')])
            
            line = line[line.index('y=')+2:]
            yInit = int(line[:line.index('..')])
            yEnd = int(line[line.index('..')+2:line.index(',')])
            
            line = line[line.index('z=')+2:]
            zInit = int(line[:line.index('..')])
            zEnd = int(line[line.index('..')+2:].strip())
            
            if xInit < -50 or xInit > 50 or yInit < -50 or yInit > 50 or zInit < -50 or zInit > 50:
                continue
            
            # print(xInit, xEnd, yInit, yEnd, zInit, zEnd)
            
            for x in range(xInit, xEnd+1):
                for y in range(yInit, yEnd+1):
                    for z in range(zInit, zEnd+1):
                        cube[midPoint+x][midPoint+y][midPoint+z] = on
        
        count = 0
        for x in range(101):
                for y in range(101):
                    for z in range(101):
                        if cube[x][y][z]:
                            count += 1
        print(count)
        
            

if __name__ == "__main__":
    solver()
    
    

