#ficheiro = 'sampleInput.txt'
#count = [0, 0, 0, 0, 0]

ficheiro = 'input.txt'
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

totalLines = 0
with open(ficheiro, 'r') as f:
    for line in f:
        for i, c in enumerate(line.strip()):
            count[i] += int(c)
        #count[0] += int(line[0])
        
        totalLines += 1

gamma = epsilon = ''
for x in count:
    if x > (totalLines - x):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
        

print(count)
print(totalLines)
print (gamma)
print(epsilon)
print(int(gamma, 2))
print(int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))