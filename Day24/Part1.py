# from Day24.alu import ALU

__ficheiro = 'input.txt'

# resultCache = {}
# alu = ALU()
# counter = 0

# def solver():
#     instructionSet = parseInput()
#     # print(instructionSet)
#
#     resultsList = [None for i in range(len(instructionSet)+1)]
#     resultsList[len(instructionSet)] = {0:0}
#
#     print(solveInstructionSetBack(instructionSet[13],[0]))
    
    # results = [0]
    # for i in range(len(instructionSet)):
    #     print(i, len(results))
    #     results = solveInstructionSet(instructionSet[i], results)
    
    # print(results)
    
    # for i in range(len(instructionSet)-1, -1, -1): 
    #     resultsList[i] = solveInstructionSet(instructionSet[i], resultsList[i+1].keys())
    #
    # # for result in resultsList:
    # print(resultsList)
    
    # print(resultsList[13])
    # print(resultsList[13].keys())
    
# def solveInstructionSet(instructionSet, possibleZValues):
#     results = set()
#     for inp in range(1,10):
#         for z in possibleZValues:
#             results.add(alu.processInstructions(instructionSet, inp, z))
#     return results
#
# def solveInstructionSetBack(instructionSet, possibleZResults):
#     results = set()
#     for inp in range(1,10):
#         for z in range(0, 10000):
#             result = alu.processInstructions(instructionSet, inp, z)
#             if result in possibleZResults:
#                 results.add((inp, z))
#     return results
    
    
    
# def cachedProcessing(instructionSet, currentInstructionBlock, inp, z):
#     # global counter
#     # counter += 1
#     if (currentInstructionBlock, inp, z) not in resultCache:
#         # print('processInstructions(', currentInstructionBlock, ',', inp, ',', z, ')')
#         resultCache[(currentInstructionBlock, inp, z)] = alu.processInstructions(instructionSet[currentInstructionBlock], inp, z)
#         # print(len(resultCache), counter)
#
#     if currentInstructionBlock == len(instructionSet)-1:
#         if resultCache[(currentInstructionBlock, inp, z)] == 0:
#             return str(inp)
#         else:
#             return None
#     else:
#         for inpRec in range(9,0,-1):
#             result = cachedProcessing(instructionSet, currentInstructionBlock+1, inpRec, resultCache[(currentInstructionBlock, inp, z)])
#             if result != None:
#                 return str(inp) + result
#         return None
    
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
                result[a[0]] = 9
                result[i] = 9 + b
            else: 
                result[a[0]] = 9 - b
                result[i] = 9
        
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
    
    

