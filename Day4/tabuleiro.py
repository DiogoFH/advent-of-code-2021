from pickle import TRUE
class Tabuleiro:
    def __init__(self):
        self.data = []
        
    def addLine(self, line):
        newLine = []
        for item in line.split():
            newLine.append(Casa(item))
        self.data.append(newLine)
    
    def print(self):
        for line in self.data:
            for casa in line:
                if casa.removido:
                    print('   ', end='')
                else:
                    print(casa.valor.rjust(2, ' '), end=' ')
            print()
            
    def remove(self, number):
        for line in self.data:
            for item in line:
                if item.valor == number:
                    item.removido = True
                    
    def hasWon(self):
        # validar linhas
        for line in self.data:
            won = True
            for casa in line:
                if not casa.removido:
                    won = False
                    break
            if won:
                return True
            
        # validar colunas
        for i in range(5):
            won = True
            for j in range(5):
                #print(self.data[j][i].valor)
                if not self.data[j][i].removido:
                    won = False
                    break
            if won:
                return True
                    
        return False
    
    def score(self):
        score = 0
        for line in self.data:
            for casa in line:
                if not casa.removido:
                    score += int(casa.valor)
        return score
                    
class Casa:
    def __init__(self, valor):
        self.valor = valor
        self.removido = False