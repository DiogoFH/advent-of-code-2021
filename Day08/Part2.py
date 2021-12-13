#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        resultado = 0
        for linha in file.readlines():
            padroes, valores = linha.split('|')
            
            padroes = descodificarPadroes(padroes.strip())
            #print(padroes)
            
            resultado += int(descodificarValores(valores.strip(), padroes))
            
        print(resultado)
        
def descodificarPadroes(padroes):
    # lista para o resultado
    resultado = [' '] * 10
    #separar os padroes e ordenar as letras lá dentro
    padroes = [normalizar(x) for x in padroes.split(' ')]
    
    resultado[1] = [x for x in padroes if len(x) == 2][0]
    resultado[4] = [x for x in padroes if len(x) == 4][0]
    resultado[7] = [x for x in padroes if len(x) == 3][0]
    resultado[8] = [x for x in padroes if len(x) == 7][0]
    
    padroes5 = [x for x in padroes if len(x) == 5]
    padroes6 = [x for x in padroes if len(x) == 6]
    
    for x in padroes5:
        if contem(x, resultado[1]):
            resultado[3] = x
            padroes5.remove(x)
            break
    
    for x in padroes6:
        if contem(x, resultado[3]):
            resultado[9] = x
            padroes6.remove(x)
            break
    
    for x in padroes6:
        if contem(x, resultado[1]):
            resultado[0] = x
            padroes6.remove(x)
            break
    
    resultado[6] = padroes6[0]
    
    for x in padroes5:
        if contem(resultado[6], x):
            resultado[5] = x
            padroes5.remove(x)
            break
    
    resultado[2] = padroes5[0]
    
    return resultado

# verifica se todos os caracteres do y estão no x
def contem(x,y):
    for c in y:
        if not c in x:
            return False
    return True

def normalizar(s):
    return ''.join(sorted(s))

def descodificarValores(valores, padroes):
    resultado = ''
    for valor in valores.split(' '):
        resultado += str(padroes.index(normalizar(valor)))
    return resultado
    
if __name__ == "__main__":
    solver()