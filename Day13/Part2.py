#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

board = []
pontos = []

def solver():
    with open(__ficheiro, 'r') as file:
        maxX = 0
        maxY = 0
        for line in file:
            if line == '\n':
                break
            ponto = tuple(map(int, line.strip().split(',', 1)))
            pontos.append(ponto)
            if ponto[0] > maxX:
                maxX = ponto[0]
            if ponto[1] > maxY:
                maxY = ponto [1]  
            
        board = [[False for elem in range(maxX+1)] for line in range(maxY+1)]
        for ponto in pontos:
            board[ponto[1]][ponto[0]] = True
            
        #printBoard(board)
        
        for line in file:
            orientation, value = line.strip()[11:].split('=')
            board = fold(board,orientation,int(value))
            #printBoard(board)
            
        printBoard(board)
        
            
def printBoard(board):
    for line in board:
        for position in line:
            if position:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
                
def fold(board, orientation, value):
    if orientation == 'x':
        return foldVertical(board, value)
    else:
        return foldHorizontal(board, value)
    
def foldHorizontal(board, value):
    for y in range(1,value+1):
        for x in range(len(board[0])):
            board[value-y][x] = board[value-y][x] or board[value+y][x]
    
    return board[:value]
    

def foldVertical(board, value):
    for x in range(1,value+1):
        for y in range(0,len(board)):
            board[y][value-x] = board[y][value-x] or board[y][value+x]
    
    return [line[:value] for line in board]

def countDots(board):
    count = 0
    for line in board:
        for position in line:
            if position:
                count += 1
    return count
    
if __name__ == "__main__":
    solver()