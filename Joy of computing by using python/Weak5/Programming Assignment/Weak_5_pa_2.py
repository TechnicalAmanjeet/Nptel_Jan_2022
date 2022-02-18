# You are given a list L. Write a function uniqueE which will return a list of unique elements is 
# the list L in sorted order. (Unique element means it should appear in list L only once.)

def uniqueE(L):
    l = []
    # print(L)
    for element in L:
        if element not in l and L.count(element) == 1:
            l.append(element)
    m =  sorted(l)
    # print(l)
    return m

L = [int(i) for i in input().split()]
print(uniqueE(L))