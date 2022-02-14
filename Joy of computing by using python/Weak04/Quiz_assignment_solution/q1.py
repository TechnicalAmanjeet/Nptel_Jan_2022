import string
import random

# print(string.ascii_letters)

A = string.ascii_letters

n = int(input(" enter number : "))

for i in range(n):
    L = []
    for j in range(n):
        L.append(random.choice(A))

    for element in L:
        print(element, end=('\t'))
    print()
