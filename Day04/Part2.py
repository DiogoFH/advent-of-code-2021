#__ficheiro = 'sampleInput.txt'
__ficheiro = 'input.txt'

from Day04.tabuleiro import Tabuleiro

def solver():
    with open(__ficheiro, 'r') as f:
        drawnNumbers = f.readline()
        tabuleiros = loadTabuleiros(f)
        
        print(drawnNumbers)
        
        for drawnNumber in drawnNumbers.split(','):
            print(drawnNumber)
            for tab in tabuleiros:
                tab.remove(drawnNumber)
            for tab in tabuleiros:
                if tab.hasWon():
                    tabuleiros.remove(tab)
                    if len(tabuleiros) == 0:
                        print(tab.score()*int(drawnNumber))
                        return
                        
        
        
def loadTabuleiros(file):
    tabuleiros = []
    file.readline()
    currTabuleiro = Tabuleiro()
    for line in file:
        if line == '\n':
            tabuleiros.append(currTabuleiro)
            currTabuleiro = Tabuleiro()
        else:
            currTabuleiro.addLine(line.strip())
    tabuleiros.append(currTabuleiro)
    return tabuleiros

if __name__ == "__main__":
    solver()