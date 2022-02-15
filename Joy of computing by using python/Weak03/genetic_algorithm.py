import random


# generate random file with 0's and 1's
# with open("file.txt", "a") as file:
#     for i in range(1000):
#         file.write(str(random.randint(0, 1)))

def evolve(x):
    for i in range(10000):
        random_number = random.randint(0, 100)
        if random_number == 1:
            index = random.randint(0, len(x)-1)
            if x[index] == '0':
                x[index] = '1'

with open("file.txt") as file:
    x = list(file.read())
    print(x)

evolve(x)
print(x)
