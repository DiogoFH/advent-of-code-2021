#__ficheiro, tamanho = 'sampleInput.txt', 10
__ficheiro, tamanho = 'input.txt', 1000

matriz = [[0 for x in range(tamanho)] for y in range(tamanho)]

def solver():
    #printMatriz()
    with open(__ficheiro, 'r') as file:
        for line in file:
            processarLinha(line.strip())
    
    #printMatriz()
    contador = 0
    for linha in matriz:
        for x in linha:
            if x > 1:
                contador += 1
            
    print(contador)

def processarLinha(line):
    pontos = line.split(' -> ')
    inicio = pontos[0].split(',')
    fim = pontos[1].split(',')
    if inicio[0] == fim[0] or inicio[1] == fim[1]:
        #horizontal ou vertical
        for x in range(min(int(inicio[0]),int(fim[0])),max(int(inicio[0]),int(fim[0]))+1):
            for y in range(min(int(inicio[1]), int(fim[1])), max(int(inicio[1]), int(fim[1]))+1):
                matriz[y][x] += 1
    else:
        #diagonal
        incrementoX = 1 if int(inicio[0]) < int(fim[0]) else -1
        incrementoY = 1 if int(inicio[1]) < int(fim[1]) else -1
        for i in range(abs( int(inicio[0]) - int(fim[0]))+1):
            matriz[int(inicio[1])+incrementoY*i][int(inicio[0])+incrementoX*i] += 1
    
def printMatriz():
    for linha in matriz:
        for x in linha:
            print(x,end='')
        print()
    print()
    
if __name__ == "__main__":
    solver()