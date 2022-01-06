__ficheiro = 'input.txt'

def solver():
    instructionSet = parseInput()
    print(instructionSet)
    
    stack = []
    lista = []
    result = [0 for i in range(14)]
    
    for i, instructions in enumerate(instructionSet):
        lista.append((i, int(instructions[3].split()[2]), int(instructions[4].split()[2]), int(instructions[14].split()[2])))
        
    for i, div, check, offset in lista:
        print(i, div, check, offset)
        if div == 1:
            stack.append((i, offset))
        else:
            a = stack.pop() 
            b = a[1] + check
            if b < 0:
                result[a[0]] = 1 - b
                result[i] = 1
            else: 
                result[a[0]] = 1
                result[i] = 1 + b
        
    print(''.join([str(a) for a in result]))
    
def parseInstruction(instructions):
    return (instructions[3].split()[2], instructions[4].split()[2], instructions[14].split()[2])
    
def parseInput():
    instructionSets = []
    instructions = []
    with open(__ficheiro, 'r') as file:
        for line in file:
            if line.startswith('inp'):
                if instructions != []:
                    instructionSets.append(instructions)
                instructions = []
            else:
                instructions.append(line.strip())
    instructionSets.append(instructions)
    return instructionSets
    

if __name__ == "__main__":
    solver()
    
    

