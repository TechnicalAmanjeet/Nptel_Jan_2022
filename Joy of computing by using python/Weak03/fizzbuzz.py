# idea is to write fizz buzz game.

# Rules for FizzBuzz Game is as follows
# R1 => ask a number from user.
# R2 => Loop from 1 till user input number and start
# R3 => printing that number except the number which is multiple of 3 and 5 or both.
# R4 => The number which is multiple of 3 => print Fizz
# R5 => The number which is multiple of 5 => print Buzz
# R5 => and at the end , the number which is multiple of both 3 and 5 write => FizzBuzz

# ******** Code starts from here **********
user_input = int(input("Enter a Number : "))  # R1

for num in range(1, user_input+1):  # R2
    print((str(num) + " : "), end=" ")  # R3

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
