# computing factorial of number using recursion.

def fect(number):
    if number == 0 or number == 1:
        return 1
    return number * fect(number - 1)

print(fect(20))