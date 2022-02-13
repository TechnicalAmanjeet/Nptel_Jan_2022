L1 = ["hp", "m", "s", "a", "jw"]
L2 = ["d", "s", "b", "dh", "r", "m"]

L = []

for i in range(len(L1)):
    flag = 0
    for j in range(len(L2)):
        if L1[i] == L2[j]:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        L.append(L1[i])
print(L)