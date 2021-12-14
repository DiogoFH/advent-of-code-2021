#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

scoreCard = {')': 3, ']': 57, '}' : 1197, '>' : 25137}

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

def solver():
    score = 0
    with open(__ficheiro, 'r') as file:
        for line in file:
            stack = []
            for c in line.strip():
                if c in openers:
                    stack.append(c)
                else:
                    if not match(stack.pop(), c):
                        score += scoreCard[c]
                        break
    
    print(score)                     
                
       
def match(opener, closer):
    if     (opener == '(' and closer == ')'
        or opener == '[' and closer == ']'
        or opener == '{' and closer == '}'
        or opener == '<' and closer == '>'):
        return True
    else:
        return False
    
if __name__ == "__main__":
    solver()