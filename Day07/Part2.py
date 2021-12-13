#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        lista = [int(val) for val in file.read().split(',')]
    
    minimo = min(lista)
    maximo = max(lista)
    minFuel = 0

    custo = []
    custo.append(0)
    for i in range(1, maximo+1):
        custo.append(custo[i-1]+i)
        
    #print(custo)
    
    for i in range(minimo, maximo):
        currFuel = 0
        for j in lista:
            currFuel += custo[abs(i - j)]
        if minFuel == 0:
            minFuel = currFuel
        else:
            if currFuel < minFuel:
                minFuel = currFuel
    
    print(minFuel)
    
if __name__ == "__main__":
    solver()