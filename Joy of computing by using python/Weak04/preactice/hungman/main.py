import os
import random
import string

from word import words # importing a list of english word from our other python file word.

# print(words)
# print(len(words))

def get_all_valid(words):
    word = random.choice(words) # getting a valid word from our distionary
    while " " in words or "-" in words:
        word.append(random.choice(words))
    # print(len(word))
    # print(word)
    return word

def hangman():
    os.system("clear")
    print("""\n   ********* Hangman Game ***********\n\n""")
    word = get_all_valid(words).upper() # taking a unique word from our dictionory
    word_letter = set(word)  # separate all letters of uniqe letter by unique alphabet
    alphabat = set(string.ascii_uppercase) # all latter of ualphabet.
    user_choice = set()
    live = 1

    # taking input from user#
    while len(word_letter)>0 and live <= len(word)*3:
        os.system("clear")
        print("""\n   ********* Hangman Game ***********\n\n""")
        print(f"you are in {live} of {len(word)*3} attempt.")
        print("you have used these letters : ",' '.join(user_choice))
        word_choice = [w if w in user_choice else '_' for w in word]
        print("Current word : ", ' '.join(word_choice))
        live = live + 1
        user_letter = input("\n Gauss a letter. : ").upper()
        if user_letter in (alphabat - user_choice):
            user_choice.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
        elif user_letter in user_choice:
            print(" you already gaussed this letter. ")
        else:
            print(" you typed a wrong character. try again.")

    if len(word_letter) == 0:
        print(f"\n you gaussed the word {word} correctly... in {live} attempts..")
    else:
        print("\n Oops you are died!!..",end=" ")
        print(f"Actual word is {word}")
    input("\n\n Press Enter to continue...")


if __name__ == "__main__":
    while 1:
        os.system("clear")
        print("""       *********** Hangman Game ********* 
           Press 1 : To play Hangman Game.
           Press 2 : To Exit from Game
        """)

        player_choice = int(input(" \n Enter YOur Choice : "))
        if player_choice == 1:
            hangman()
        else:
            break


