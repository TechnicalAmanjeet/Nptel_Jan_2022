import random

from PIL import Image

MAX = 100
lader_list = [[i, i] for i in range(1, 100)]
# print(lader_list)

def initialize_ladder():
    global  lader_list
    lader_list = [[i, i] for i in range(1, 100)]
    lader_list[12] = ["l", 66]
    lader_list[34] = ["l", 58]
    lader_list[73] = ["l", 91]
    lader_list[66] = ["l", 100]

    lader_list[88] = ["s", 76]
    lader_list[74] = ["s", 52]
    lader_list[46] = ['s', 12]
    lader_list[25] = ["s", 6]



def show_image():
    """Will show the snake game board."""
    img = Image.open("./snake_board.png")
    img.show()

# show_image()

def check(number):
    global lader_list
    if lader_list[number][0] == number:
        return number
    else:
        return lader_list[number][1]

def win(num, comp):
    if num == 100:
        return True


def play():
    initialize_ladder()
    show_image()
    global lader_list
    print(lader_list)
    p1 = input("\nEnter player Name : ")
    term = 0
    comp = 0
    player = 0
    comp_value = 0
    player_value = 0

    while comp != 100 or player != 100:
        print(f"\nComputer is at : {comp}")
        comp_value = random.randint(1, 6)
        print(f"Computer turn : {comp_value}")
        if comp + comp_value <= 100:
            comp += comp_value
        comp = check(comp)
        if win(comp, comp_value):
            print("Computer is a winner!!")
            return

        input("\nPlease press enter key to your turn => ")
        print(f"{p1} is at : {player}")
        player_value = random.randint(1, 6)
        print(f"Player turn : {player_value}")
        if player + player_value <= 100:
            player += player_value
        player = check(player)

        if win(player, player_value):
            print(f"{p1} has win the game!!")
            return

        print(f"\nComp : {comp} & {p1} : {player}")
        input("press enter key for next move.")

play()