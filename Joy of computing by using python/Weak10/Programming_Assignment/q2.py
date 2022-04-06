import math


def closestSchool(x, y, L):
    out = []
    distList = []

    for lst in L:
        dist = round(math.sqrt( math.pow(x-lst[0], 2) + math.pow(y-lst[1], 2)), 2)
        # print(dist)
        distList.append(dist)

    # print(distList)
    sortedDistList = sorted(distList)
    # print(sortedDistList)
    outNumber = distList.count(sortedDistList[0])
    # print(outNumber)
    stNum = 0
    endNum = len(distList)

    for i in range(outNumber):
        member = distList.index(sortedDistList[0], stNum, endNum)
        out.append(L[member])
        print(out[i])
        stNum = i + 1

x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)
