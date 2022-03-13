n = 10
L = list(map(int, input().split()))

for w in L:
    if w == 0:
        L.remove(0)
        L.append(0)
print(L)