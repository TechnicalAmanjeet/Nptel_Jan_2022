# will built tic tac too game from scratch here.
import numpy
import numpy as np

square_board = np.array([["_", '_', '_'], ["_", '_', '_'], ["_", '_', '_']])

def initalize_square_board():
    square_board = np.array([["_", '_', '_'], ["_", '_', '_'], ["_", '_', '_']])


def print_square_board(square_board):
    """Will print square board on screen."""
    for item in square_board:
        print(item)


def enter_your_position(chance, player):
    """user will enter position in square board where he wants to put the value."""
    print_square_board(square_board)
    while True:
        row = int(input(f"\n{player}, Please enter row of Square board ( 1 , 2 or 3 ) : "))
        col = int(input(f"{player}, Please enter col of Square board ( 1 , 2 or 3 ) : "))

        if square_board[row-1][col-1] == '_' and row in [1, 2, 3] and col in [1, 2, 3]:
            square_board[row - 1][col - 1] = chance
            break
        else:
            print("You choose a wrong place to fill! please look at matrix carefully and then enter value!!")


def winner(chance):
    win = False
    if square_board[0][0] == square_board[0][1] and square_board[0][1] == square_board[0][2] and square_board[0][2] == chance:
        win = True
    elif square_board[1][0] == square_board[1][1] and square_board[1][1] == square_board[1][2] and square_board[1][2] == chance:
        win = True
    elif square_board[2][0] == square_board[2][1] and square_board[2][1] == square_board[2][2] and square_board[2][2] == chance:
        win = True
    elif square_board[0][0] == square_board[1][0] and square_board[1][0] == square_board[2][0] and square_board[2][0] == chance:
        win = True
    elif square_board[0][1] == square_board[1][1] and square_board[1][1] == square_board[2][1] and square_board[2][1] == chance:
        win = True
    elif square_board[0][2] == square_board[1][2] and square_board[1][2] == square_board[2][2] and square_board[2][2] == chance:
        win = True
    elif square_board[0][0] == square_board[1][1] and square_board[1][1] == square_board[2][2] and square_board[2][2] == chance:
        win = True
    elif square_board[0][2] == square_board[1][1] and square_board[1][1] == square_board[0][2] and square_board[0][2] == chance:
        win = True
    return win



def play():
    """Game  will start from here.."""
    global square_board
    initalize_square_board()
    p1 = input("Enter player1 name ( will take O ) : ")
    p2 = input("Enter player2 name ( will take * ) :  ")
    chance = 'o'
    for chan in range(9):
        if chan % 2 == 0:
            print(f"\n{p1}'s Turn ( o )=> ")
            chance = "O"
            enter_your_position(chance, p1)
        else:
            print(f"\n{p2}'s Turn ( * ) => ")
            chance = '*'
            enter_your_position(chance, p2)
        if winner(chance):
            if chan % 2 == 0:
                print(f"\n**** {p1} have won the match !!! *****")
            else:
                print(f"\n******* {p2}  have won the match!!!!!!! ******")
            return
    print("\n**** Draw !!!!! ******")


game_is_on = True

while game_is_on:
    play()
    while True:
        user_input = input("\nDo you want to play this game again? (y/n) : ")
        if user_input == 'y':
            game_is_on = True
            break
        elif user_input == 'n':
            game_is_on = False
            break
        else:
            print("\nYou Choose a wrong key!!!")
print("\n ********** Thank you so much for playing this game **********")