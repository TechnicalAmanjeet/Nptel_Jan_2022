def recursive(L):
    return recursive(L[:-1]) * L[-1]

print(recursive([1,2,3,4,5,6,7,8,9,10]))