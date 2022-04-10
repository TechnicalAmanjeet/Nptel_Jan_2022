# implementation of linear search
import random

list = []

for i in range(15):
    list.append(random.randint(1, 20))

sorted_list = sorted(list)
print(list)
print(sorted_list)

def binary_sort(list, key):
    start = 0
    end = len(list)-1


    while start < end:
        mid = (start + end)//2
        print(start, end)
        if list[mid] == key:
            print(f"{key} is present in list.")
            return
        elif list[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    # print(start, mid)
    print(f"{key} is not present in the list...")

key = 10
binary_sort(sorted_list, key)



