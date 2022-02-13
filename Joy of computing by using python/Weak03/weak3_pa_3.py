
def all_even(L):
    for element in L:
        if element % 2 == 0:
            print(element)

L = [int(i) for i in input().split()]
all_even(L)