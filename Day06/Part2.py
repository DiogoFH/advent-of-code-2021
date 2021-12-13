#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        lista = [int(val) for val in file.read().split(',')]
    
    listaOptimizada = []
    for i in range(9):
        listaOptimizada.append(lista.count(i)) 
    
    print(listaOptimizada)
    
    for i in range(256):
        carry = 0
        for j in range(8, -1, -1):
            aux = listaOptimizada[j]
            listaOptimizada[j] = carry
            carry = aux
            
        listaOptimizada[8] = aux
        listaOptimizada[6] += aux
        #print(listaOptimizada)
    
    print(sum(listaOptimizada))
    
if __name__ == "__main__":
    solver()