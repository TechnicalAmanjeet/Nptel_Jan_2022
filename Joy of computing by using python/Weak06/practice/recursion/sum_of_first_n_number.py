# sum of first n number by using recursion.

def sum_of_N(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return num + sum_of_N(num-1)

print(sum_of_N(10))