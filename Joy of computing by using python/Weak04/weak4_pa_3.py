L = [int(i) for i in input().split()]

output = []

for number in L:
    if L.count(number) == 2 and number not in output:
        print(number)
        output.append(number)
