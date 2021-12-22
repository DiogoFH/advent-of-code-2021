#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

def solver():
    state = parseInput()
    
    # printState(state)
    
    diceDistribution = [0,0,0,1,3,6,7,6,3,1]
    
    currentPlayer = 0
    while not endGame(state):
    # for turn in range(5):
        newState = [[[[0 for i in range(22)] for j in range(10)] for k in range(22)] for l in range(10)]
        for position1 in range(10):
            for score1 in range(22):
                for position2 in range(10):
                    for score2 in range(22):
                        numUniversos = state[position1][score1][position2][score2]
                        if numUniversos > 0:
                            if score1 == 21:
                                newState[position1][score1][position2][score2] += numUniversos
                            elif score2 == 21:
                                newState[position1][score1][position2][score2] += numUniversos
                            else:
                                for diceRoll, distribution in enumerate(diceDistribution):
                                    if diceRoll > 0 and distribution > 0:
                                        if currentPlayer == 0:
                                            newPosition1 = (position1 + diceRoll) % 10
                                            newScore1 = score1 + (newPosition1 if newPosition1 != 0 else 10)
                                            if newScore1 > 21:
                                                newScore1 = 21
                                            newState[newPosition1][newScore1][position2][score2] += (numUniversos * distribution)
                                        else:
                                            newPosition2 = (position2 + diceRoll) % 10
                                            newScore2 = score2 + (newPosition2 if newPosition2 != 0 else 10)
                                            if newScore2 > 21:
                                                newScore2 = 21
                                            newState[position1][score1][newPosition2][newScore2] += (numUniversos * distribution)
                                    
        
        state = newState
        currentPlayer = (currentPlayer + 1) % 2
        # print(countUniverses(state))
    
    # printState(state)
    print(countWins(state))
    
def countUniverses(state):
    universes = 0
    for position1 in range(10):
        for score1 in range(22):
            for position2 in range(10):
                for score2 in range(22):
                    universes += state[position1][score1][position2][score2]
    return universes
    
    
def countWins(state):
    player1Wins = player2Wins = 0
    for position1 in range(10):
        for score1 in range(22):
            for position2 in range(10):
                for score2 in range(22):
                    if score1 == 21:
                        if score2 == 21:
                            if state[position1][score1][position2][score2] != 0:
                                print('Erro? Position1: ', position1, ' Score1: ', score1, 'Position2: ', position2, ' Score2: ', score2, ' Universes: ', state[position1][score1][position2][score2])
                        player1Wins += state[position1][score1][position2][score2]
                    elif score2 == 21:
                        player2Wins += state[position1][score1][position2][score2]
                    else:
                        if state[position1][score1][position2][score2] != 0:
                            print('Erro? Position1: ', position1, ' Score1: ', score1, 'Position2: ', position2, ' Score2: ', score2, ' Universes: ', state[position1][score1][position2][score2]) 
    
    return player1Wins, player2Wins 

def endGame(state):
    for position1 in range(10):
        for score1 in range(21):
            for position2 in range(10):
                for score2 in range(21):
                    if state[position1][score1][position2][score2] != 0:
                        return False
    return True     

def printState(state):
    for position1 in range(10):
        for score1 in range(22):
            for position2 in range(10):
                for score2 in range(22):
                    if state[position1][score1][position2][score2] != 0:
                        print('Position1: ', position1, ' Score1: ', score1, 'Position2: ', position2, ' Score2: ', score2, ' Universes: ', state[position1][score1][position2][score2])
        
    print()

def parseInput():
    with open(__ficheiro, 'r') as file:
        playersScorePosition = [[[[0 for i in range(22)] for j in range(10)] for k in range(22)] for l in range(10)]
        
        line = file.readline().strip()
        player1Start = int(line[-1])
        line = file.readline().strip()
        player2Start = int(line[-1])
        
        playersScorePosition[player1Start][0][player2Start][0] = 1
    return playersScorePosition


if __name__ == "__main__":
    solver()
    
    

