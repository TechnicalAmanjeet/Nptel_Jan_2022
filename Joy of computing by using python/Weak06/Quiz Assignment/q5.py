def recursive(L):
    if len(L) == 1:
        return L[0]
    return L[0] + recursive(L[1:])

print(recursive(range(1,11)))
print(recursive([1,2,3,4,5,6,7,8,9,10]))