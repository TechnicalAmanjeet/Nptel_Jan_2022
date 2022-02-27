# Binary Search.

def Binary(L, find, start, end):
    mid = int((start + end) / 2)

    if start == end:
        if L[end] == find:
            return end
        else:
            return -1

    elif L[mid] == find:
        return mid

    elif find > mid:
        return Binary(L, find, mid+1, end)
    else:
        return  Binary(L, find, start, mid - 1)


l = [1,2,3,4,5,6,7,8,9,10]
print(Binary(l, -12, 0, len(l)-1))
