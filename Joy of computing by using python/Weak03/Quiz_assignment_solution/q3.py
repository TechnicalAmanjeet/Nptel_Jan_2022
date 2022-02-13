import random

L = []
for i in range(10):
    L.append(random.randint(0, 10))

L.sort()
L.reverse()

print(L)