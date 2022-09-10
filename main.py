from SudokuTable import SudokuTable

stable = open("table1.txt")
tablel = stable.readlines()

stable.close

tb = SudokuTable(tablel)


tb.printTable()



