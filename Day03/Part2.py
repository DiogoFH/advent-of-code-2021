#__ficheiro = 'sampleInput.txt'

__ficheiro = 'input.txt'

def solver():
    ogr = []
    co2sr = []
    with open(__ficheiro, 'r') as f:
        for line in f:
            ogr.append(line.strip())
            co2sr.append(line.strip())
    #print(oxigenGeneratorRating(ogr))
    #print(co2ScrubberRating(co2sr))
    print(int(oxigenGeneratorRating(ogr), 2) * int(co2ScrubberRating(co2sr), 2))

def oxigenGeneratorRating(lista):
    i = 0
    while len(lista) > 1:
        lista = filtrar(lista, i, maisComum(lista, i))
        i += 1
    return lista[0]        
        
def co2ScrubberRating(lista):
    i = 0
    while len(lista) > 1:
        lista = filtrar(lista, i, menosComum(lista, i))
        i += 1
    return lista[0]
        
def filtrar(lista, index, valor):
    filtrada = []
    for item in lista:
        if item[index] == valor:
            filtrada.append(item)
    return filtrada

def maisComum(lista, index):
    count = 0
    for item in lista:
            count += int(item[index])
    if count >= (len(lista) - count):
        return '1'
    else:
        return '0'

def menosComum(lista, index):
    count = 0
    for item in lista:
            count += int(item[index])
    if count < (len(lista) - count):
        return '1'
    else:
        return '0'


if __name__ == "__main__":
    solver()