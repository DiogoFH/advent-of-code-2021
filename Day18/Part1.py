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
        number = parseLine(file.readline())

        # print(number)
        for line in file.readlines():
            currNumber = parseLine(line)
            # print(currNumber)
            number += currNumber
            # print(number)
            
        print(number)
        print(number.magnitude())


def reduce(number):
    return number

def parseLine(line):
    return  SnailfishNumber(ast.literal_eval(line), None)

if __name__ == "__main__":
    solver()