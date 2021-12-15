#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        polymer = file.readline().strip()
        # print(polymer)
        
        file.readline()
        
        mapa = dict(line.strip().split(' -> ') for line in file)
        # print(mapa)
        
        for step in range(10):
            newPolymer = ''
            for item in zip(polymer, polymer[1:]):
                # print(item)
                newPolymer += item[0]
                if item[0] + item[1] in mapa:
                    newPolymer += mapa[item[0] + item[1]]
            polymer = newPolymer + polymer[-1:] 
            
        #print(polymer)
        
        max = 0
        min = -1
        for c in set(polymer):
            count = polymer.count(c)
            if min == -1:
                min = count
            elif min > count:
                min = count
            
            if max < count:
                max = count
                
        print(max-min)
            
        
            

if __name__ == "__main__":
    solver()