import math

#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

scoreCard = {')': 1, ']': 2, '}' : 3, '>' : 4}

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

def solver():
    scores = []
    with open(__ficheiro, 'r') as file:
        for line in file:
            stack = []
            for c in line:
                if c == '\n':
                    #print('EOL:', stack)
                    completion = ''
                    stack.reverse()
                    for c in stack:
                        completion += closers[openers.index(c)]
                    #print(completion)
                    scores.append(lineScore(completion))
                    
                elif c in openers:
                    stack.append(c)
                else:
                    if match(stack.pop(), c):
                        continue
                    else:
                        #corrupted
                        break
    scores.sort()
    
    print(scores[math.floor(len(scores)/2)])                     
    
       
def match(opener, closer):
    if     (opener == '(' and closer == ')'
        or opener == '[' and closer == ']'
        or opener == '{' and closer == '}'
        or opener == '<' and closer == '>'):
        return True
    else:
        return False
    
def lineScore(line):
    score = 0
    for c in line:
        score = score * 5 + scoreCard[c] 
    return score
    
if __name__ == "__main__":
    solver()