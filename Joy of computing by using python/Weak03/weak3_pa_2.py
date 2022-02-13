L = [int(i) for i in input().split()]  # taking input from user through cmd.

L.sort()

smallest_element_in_ascending = [L[0], L[1], L[2]]
greatest_element_in_decending = [L[-1], L[-2]]

print(smallest_element_in_ascending)
print(greatest_element_in_decending)
