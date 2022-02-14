import string
import random

L = ["harry potter", "matrix", "spide-rman"]

sc = string.ascii_letters+"0123456789"
# print(sc)

movie = random.choice(L)
print(movie)

for ch in movie:
    if ch in sc:
        print("*", end="")
    else:
        print(ch, end="")