#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

diceRoll = 0

def solver():
    with open(__ficheiro, 'r') as file:
        line = file.readline().strip()
        playerPos = [int(line[-1])]
        line = file.readline().strip()
        playerPos.append(int(line[-1]))
        
        playerScore = [0, 0]
        
        print(playerPos)
        print(playerScore)
        
        totalDiceRolls = 0
        currentPlayer = 0
        
        while playerScore[0] < 1000 and playerScore[1] < 1000:
            totalDiceRolls += 3
            totalDiceRoll = rollDice() + rollDice() + rollDice()
            playerPos[currentPlayer] = (playerPos[currentPlayer] + totalDiceRoll) % 10
            
            playerScore[currentPlayer] += (playerPos[currentPlayer] if playerPos[currentPlayer] != 0 else 10)  
            
            currentPlayer = (currentPlayer + 1) % 2
            
        print(playerScore)
        print(totalDiceRolls)
        if playerScore[0] > playerScore[1]:
            print(playerScore[1] * totalDiceRolls)
        else:
            print(playerScore[0] * totalDiceRolls)
            
def rollDice():
    global diceRoll 
    diceRoll = diceRoll % 100 +1
    return diceRoll

if __name__ == "__main__":
    solver()
    
    

