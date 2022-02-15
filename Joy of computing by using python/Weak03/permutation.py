import itertools
import random


def make_permutation(question):
    choice = 0
    length = len(question)

    for permutation in itertools.permutations(question):
        choice += 1
        if choice == length:
            return permutation


def play():
    player1 = input("Enter name of first player : ")  # taking first player name.
    player2 = input("Enter name of second player : ")  # taking second player name.

    # assigning both player 1 and 2 as 0.
    score_p1 = 0
    score_p2 = 0
    game_turn = 0  # when game turn is even then player1 turn and p2 has to answer. True for vice-versa.
    # question = ""

    while True:
        print()
        if game_turn % 2 == 0:  # that means player1 turn and player2 to answer.
            question = input(f"Enter a word ( by {player1} ) : ").lower()  # here we can pick word randomly from a wordlist
            question_permutation = make_permutation(question)  # this function will return one of the permutation of
            # word
            print(question_permutation)
            answer = input(f"what's the correct word ( by {player2} ) : ").lower()

            if answer == question:
                score_p2 += 1
        else:
            question = input(f"Enter a word ( by {player2} ) : ").lower()
            question_permutation = make_permutation(question)
            print(question_permutation)

            answer = input(f"What's the correct word ( by {player2} : ")

            if answer == question:
                score_p1 += 1

        game_turn += 1

        if game_turn == 10:
            print(f"\nPlayer1 score : {score_p1} \n Player2 score : {score_p2}")
            if score_p1 == score_p2:
                print("Match is tie!!")
            elif score_p1 > score_p2:
                print(f"{player1} has won the match!!!")
            else:
                print(f"{player2} has won the match!!!")
            print("******** Thank you so much for playing this game **********")
            break


play()


# ******* rough work ********
# name = "cut"
# name_list = [str for str in name]
# n = itertools.permutations(name)
# n1 = itertools.permutations(name_list)
# # print(itertools.permutations(name_list))
# print(n)
# print(n1)
#
# for permutation in n:
#     print(permutation)

# output = n[0]
