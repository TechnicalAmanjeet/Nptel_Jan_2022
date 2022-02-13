import random

L = ["harry potter", "matrix", "spiderman"]

movie = random.choice(L)
count = 0

for character in movie:
    if character == 'a':
        count += 1
    elif character == 'e':
        count += 1
    elif character == 'i':
        count += 1
    elif character == 'o':
        count += 1
    elif character == 'u':
        count += 1
print(count, movie)