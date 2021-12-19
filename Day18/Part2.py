import ast
from Day18.snailfishNumber import SnailfishNumber

#__ficheiro = 'sampleInput.txt'
#__ficheiro = 'sampleInput2.txt'
#__ficheiro = 'sampleInput3.txt'
#__ficheiro = 'sampleInput4.txt'
#__ficheiro = 'sampleInput5.txt'
#__ficheiro = 'sampleInput6.txt'
#__ficheiro = 'sampleInput7.txt'
__ficheiro = 'input.txt'

def solver():
    with open(__ficheiro, 'r') as file:
        numberList = []
        for line in file:
            numberList.append(line)
            
        maxMagnitude = 0
        for i in range(len(numberList)):
            for j in range(len(numberList)):
                if numberList[i] != numberList[j]:
                    currentSum = parseLine(numberList[i]) + parseLine(numberList[j])
                    magnitude = currentSum.magnitude()
                    if magnitude > maxMagnitude:
                        maxMagnitude = magnitude
                        # print('New maxMagnitude:', maxMagnitude, 'from adding', numberList[i], 'and', numberList[j], 'with result', currentSum)
                        
                        

        print(maxMagnitude)


def reduce(number):
    return number

def parseLine(line):
    return  SnailfishNumber(ast.literal_eval(line), None)

if __name__ == "__main__":
    solver()