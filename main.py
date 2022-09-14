from SudokuTable import SudokuTable

stable = open("savedGame.txt")
tablel = stable.readlines()

stable.close

tb = SudokuTable(tablel)

def menu():
    print("---- BEM VINDO AO SUDOKU! ----")
    print("----   1 - NOVO JOGO      ----")
    print("----   2 - CARREGAR JOGO  ----")
    print("----   2 - SAIR           ----")
    print("------------------------------")
    op = input()
    return op

def tableMenu():
    print("----   BEM VINDO AO SUDOKU!  ----")
    print("----   1 - Adicionar Jogada  ----")
    print("----   2 - Remover Jogada    ----")
    print("----   3 - Salvar Jogo       ----")
    print("----   4 - Conferir Jogo     ----")
    print("----   5 - Voltar            ----")
    print("----   6 - Sair              ----")
    print("---------------------------------")
    op = input()
    return op
