# implementation of bubble sort.

unsorted_list = [2, 1, 5, 3, 7, 6, 8, 4, 9]


def swap(unsorted_list, i, j):
    temp = unsorted_list[i]
    unsorted_list[i] = unsorted_list[j]
    unsorted_list[j] = temp

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(1, len(unsorted_list)):
            if unsorted_list[j - 1] > unsorted_list[j]:
                swap(unsorted_list, j - 1, j)
            print(unsorted_list)
        print()

bubble_sort(unsorted_list)
print(unsorted_list)
