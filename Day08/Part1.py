#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        listaTmp = [val[val.index('|')+2:].strip() for val in file.readlines()]
        
        
    lista = []
    for x in listaTmp:
        lista += x.split(' ')
    
    #print(lista)
    
    print(len([x for x in lista if len(x) in (2,3,4,7)]))
    
    
if __name__ == "__main__":
    solver()