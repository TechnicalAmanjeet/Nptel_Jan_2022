def recursive(L):
    if len(L) <= 6:
        return L[-1]
    return L[-1] * recursive(L[:-1])

print(recursive([2,2,2,2,2,2,2]))