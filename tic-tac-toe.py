import random
L = []

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in board:

        for j in i:
            print(j,end=' ')
        print()


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        um = int(input('Enter your move 1-9: '))
        if um in range(1,10) and um not in L:
            break
        else:
            print('Wrong move, try again!')

    for i in range(len(board)):
        for j in range(len(board[i])):
            if um == board[i][j]:
                board[i][j] = 'O'
    L.append(um) 
    return display_board(board)
            

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    vl = []
    global victory
    for i in board:
        for j in i:
            if i[0] == i[1] == i[2]:
                victory = True
    for i in board:
        vl.append(i[0])
    if vl[0] == vl[1] == vl[2]:
        victory = True
    vl2 = [[board[0][0],board[1][1],board[2][2]],[board[2][0],board[1][1],board[0][2]]]
    if vl2[0][0] == vl2[0][1] == vl2[0][2] or vl2[1][0] == vl2[1][1] == vl2[1][2]:
        victory = True
    if victory:
        if sign == 'X':
            print("Computer won!\nBetter luck next time.")
        elif sign == 'O':
            print("Congratulations! You won!")
                

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        cm = random.randint(1,9)
        if cm not in L:
            break
    for i in range(len(board)):
        for j in range(len(board[i])):
            if cm == board[i][j]:
                board[i][j] = 'X'
    L.append(cm)
    return display_board(board)


board = [[1,2,3],[4,5,6],[7,8,9]]

victory = False
while True:
    print("***TIC-TAC-TOE***")
    ans = input("Shall we play? (Y/N): ")
    if ans not in 'Yy':
        break
    else:
        display_board(board)
        print("------")
    while not victory:
        draw_move(board)
        print("------")
        victory_for(board,'X')
        if victory:
            break 
        enter_move(board) 
        print("------") 
        victory_for(board,'O')
    end = int(input("Enter 0 to exit: "))
    if end == 0:
        break
