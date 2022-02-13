def sum_of_l(L):
    total = 0
    for element in L:
        total += element
    return total


L = range(1, 11)

total_sum = sum_of_l(L)

print(total_sum)
