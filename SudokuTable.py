from tabulate import tabulate

class SudokuTable:
    sudoku = []
    sudokuSolved = []
    
    def __init__(self, table):
        solvedTable = 0
        
        for line in table:
            temp = []
            
            #checa se mudou de tabela
            if line == "\n":
                solvedTable = 1
                continue
            
            
            for c in line:
                if c != "\n":
                    if c == ".":
                        temp.append("")
                    else:
                        temp.append(c)
                        
            if solvedTable == 0:
                self.sudoku.append(temp)
            else:
                self.sudokuSolved.append(temp)
    
    def printTable(self):
        print(tabulate(self.sudoku, tablefmt='fancy_grid'))
        
    def isFixedPosition(self, line, row):
        if self.sudoku[line][row] == self.sudokuSolved[line][row]:
            return True
        else:
            return False
    
    def addNumber(self, line, row, value):
        if self.isFixedPosition(line, row):
            print("Fixed Position!")
        else:
            self.sudoku[line][row] = value

    def removeNumber(self, line, row):
        if self.isFixedPosition(line, row):
            print("Fixed Position!")
        else:
            self.sudoku[line][row] = ""