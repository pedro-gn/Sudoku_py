from tabulate import tabulate
import copy
class SudokuTable:
    sudoku = []
    sudokuSolved = []
    mask = []
    
    def __init__(self, table):
        currentTable = 0
        
        for line in table:
            temp = []
            
            #checa se mudou de tabela
            if line == "\n":
                currentTable += 1
                continue
            
            
            for c in line:
                if c != "\n":
                    if c == ".":
                        temp.append("")
                    else:
                        temp.append(c)
                        
            if currentTable == 0:
                self.sudoku.append(temp)
            elif currentTable == 1:
                self.sudokuSolved.append(temp)
            else:
                self.mask.append(temp)
                
        self.mask = copy.deepcopy(self.sudoku)
        
    def printTable(self):
        print(tabulate(self.sudoku, tablefmt='fancy_grid'))
        
    def isFixedPosition(self, line, row):
        if self.mask[line-1][row-1] != "":
            return True
        else:
            return False
    
    def addNumber(self, line, row, value):
        if self.isFixedPosition(line, row):
            print("Fixed Position!")
        else:
            self.sudoku[line-1][row-1] = value

    def removeNumber(self, line, row):
        if self.isFixedPosition(line, row):
            print("Fixed Position!")
        else:
            self.sudoku[line-1][row-1] = ""
            
    def isGameCorrect(self):
        for i, line in enumerate(self.sudoku) :
            for j, c in enumerate(line) :
                if c == self.sudokuSolved[i][j] :
                    continue
                else:
                    print("Game is incorrect")
                    return False
        print("Game is Correct ! Congrats!")
        return True
    
    def saveGame(self,name):
        with open(name + ".txt", "w") as f:
            
            for line in self.sudoku :
                for c in line :
                    if c == "":
                        f.write(".")
                    else:
                        f.write(str(c))
                f.write("\n")
            f.write("\n")
            
            for line in self.sudokuSolved :
                for c in line :
                    if c == "":
                        f.write(".")
                    else:
                        f.write(str(c))                    
                f.write("\n")
            f.write("\n")
            
            for line in self.mask :
                for c in line :
                    if c == "":
                        f.write(".")
                    else:
                        f.write(str(c))
                f.write("\n")


