L = [100, 2, 5, 4,15, 3, 9, 7, 8, 10]

def test(L):
    for i in range(len(L)-1):
        for j in range(len(L)-1):
            if L[j] < L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    print(L[0])


test(L)