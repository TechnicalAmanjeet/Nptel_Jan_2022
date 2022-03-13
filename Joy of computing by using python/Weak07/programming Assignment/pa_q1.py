def DiagCalc(M):
    sum = 0
    length = len(M)

    for i in range(length):
        sum = sum + M[i][i]
    print(sum)

    sum = 0
    j = length - 1
    for i in range(length):
        sum = sum + M[i][j - i]

    print(sum)




n = int(input())
M = []
for i in range(n):
    L = list(map(int, input().split()))
    M.append(L)

DiagCalc(M)