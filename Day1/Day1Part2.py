count = 0
last = 1000000
with open('input.txt', 'r') as f:
    lines = f.read().splitlines() 
    
    print(lines)
    
    for item in zip(lines, lines[1:], lines[2:]):
        #print(item)
        soma = int(item[0])+int(item[1])+int(item[2])
        #print(soma)
        if soma > last:
            count = count + 1
        last = soma
print (count)
    