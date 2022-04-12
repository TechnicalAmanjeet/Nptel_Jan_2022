import math

list = []

for i in range(3):
    list.append(int(input()))
list.sort()

if math.pow(list[0], 2) + math.pow(list[1], 2) == math.pow(list[2], 2):
    print("YES")
else:
    print("NO")