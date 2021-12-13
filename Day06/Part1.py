#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        lista = [int(val) for val in file.read().split(',')]
    
    #print(lista)
    
    for i in range(80):
        for j in range(len(lista)):
            if lista[j] == 0:
                lista[j] = 6
                lista.append(8)
            else:
                lista[j] -= 1
    
        #print(lista)

    print(len(lista))
    
if __name__ == "__main__":
    solver()