

def binary_search(list, start, end, key):
    if end < start:
        print(f"{key} is not present in list")
        return False
    mid = (start + end)//2
    if list[mid] == key:
        print(f"{key} is present in list")
        return True
    elif list[mid] > key:
        binary_search(list, start, mid-1, key)
    else:
        binary_search(list, mid+1, end, key)

list = [1,2,3,4,5,6,7,8,9,10]
binary_search(list, 0, len(list)-1, 9)