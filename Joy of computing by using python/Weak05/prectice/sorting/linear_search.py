# implementation of linear search
import random

list = []

for i in range(15):
    list.append(random.randint(1, 20))

def linear_search(list, key):
    for member in list:
        if key == member:
            print(f"{key} is in the list.")
            return
    print(f"{key} is not present in the list.")

key = 10
linear_search(list, 10)
print(list)

