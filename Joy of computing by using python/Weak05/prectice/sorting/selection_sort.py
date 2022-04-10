# implementation of selection sort.

unsorted_list = [2, 1, 5, 3, 7, 6, 8, 4, 9]


def swap(unsorted_list, i, j):
    temp = unsorted_list[i]
    unsorted_list[i] = unsorted_list[j]
    unsorted_list[j] = temp


for i in range(1, len(unsorted_list)):
    for j in range(i, len(unsorted_list)):
        if unsorted_list[i-1] > unsorted_list[j]:
            swap(unsorted_list, i-1, j)
            print(unsorted_list)

print(unsorted_list)
