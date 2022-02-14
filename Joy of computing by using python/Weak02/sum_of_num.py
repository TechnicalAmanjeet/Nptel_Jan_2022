# idea is to find sum till user input number from 1

user_input = int(input("Enter a number : "))
sum_of_num = 0

for number in range(1, user_input + 1):
    print(number)
    sum_of_num = sum_of_num + number

print(f"Sum of number from 1 to {user_input} is {sum_of_num}.")
