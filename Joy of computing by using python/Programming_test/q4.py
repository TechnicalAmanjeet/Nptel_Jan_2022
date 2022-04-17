m = list(map(int, input().split()))

m.sort()
n = 0
b = []

while(True):
    if sum(b) < sum(m):
        b.append(m.pop())
        n +=1
    else:
        break

print(n)