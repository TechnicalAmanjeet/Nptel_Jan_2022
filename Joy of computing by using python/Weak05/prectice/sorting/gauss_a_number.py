import random

# implementation of binary search. by using a game.

START_NUMBER = 0
END_NUMBER = 100

def gauss():
    pass

def do_you_want_to_play_again():
    """Return true => user want to play game again else return false."""

    user_input = input("\n\nDo you want to play game again? (y/n) : ")
    if user_input == 'y':
        return True
    elif user_input == 'n':
        print("\n\n ***** Thank you so much for playing this game ********** ")
        return False
    else:
        print("\nYou have entered wrong choice please correct it.")
        return do_you_want_to_play_again()

def set_initial_and_final_value_of_game():
    """ Will return initial and final value for this game else it will return by default
    value of initial = 0 and final value = 100"""
    user_input = input("Do you want to set initial and final value for game? (y/n) : ")
    global START_NUMBER
    global END_NUMBER
    if user_input == 'y':
        START_NUMBER = int(input("Enter initial number : "))
        END_NUMBER = int(input("Enter End Number : "))
    elif user_input == 'n':
        return
    else:
        print("\nYou entered wrong choice? please try again...")
        set_initial_and_final_value_of_game()


def play():
    global START_NUMBER
    global END_NUMBER
    no_of_chance = 10
    user_choice = []
    set_initial_and_final_value_of_game()
    actual_number = random.randint(START_NUMBER, END_NUMBER)
    while no_of_chance > 0:
        user_number = int(input(f"Enter a number b/w {START_NUMBER} - {END_NUMBER} : "))
        if user_number == actual_number:
            print(f"\n ******** hay you are correct (in {no_of_chance}).*******")
            print(f"\n Actual number : {actual_number}")
            return
        elif user_number > actual_number:
            print(f"{user_number} is greater then the actual number")
        else:
            print(f"{user_number} is less the actual number..")
        user_choice.append(user_number)
        print(f"You Entered : {user_choice}")
        no_of_chance -= 1
    print(f"\n Actual number : {actual_number}")
    print("You loss.")


game_is_on = True

while game_is_on:
    play()
    game_is_on = do_you_want_to_play_again()