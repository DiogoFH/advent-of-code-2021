#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        polymer = file.readline().strip()
        # print(polymer)
        
        file.readline()
        
        mapa = dict(line.strip().split(' -> ') for line in file)
        # print(mapa)
        for k,v in mapa.items():
            mapa[k] = [k[0] + v, v+k[1]]
            
        # print(mapa)
        
        count = {x: 0 for x in mapa.keys()}
        
        
        for item in zip(polymer, polymer[1:]):
            count[item[0] + item[1]] += 1 
        # print(count)
        
        for step in range(40):
            newCount = {x: 0 for x in mapa.keys()}
            for k,v in count.items():
                for a in mapa[k]:
                    newCount[a] += v
            count = newCount 
        
        totals = {}
        for k,v in count.items():
            if k[0] not in totals:
                totals[k[0]] = v
            else:
                totals[k[0]] += v
            
        totals[polymer[-1]] += 1
        
        print(totals)
        print(max(totals.values()) - min(totals.values()))
            

if __name__ == "__main__":
    solver()