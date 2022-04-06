L = list(map(int, input().split()))
L.sort()

out = []
for i in range(L[-1]+1):
    if i in L:
        out.append(i)
    else:
        out.append(0)
    print(out[i], end=" ")