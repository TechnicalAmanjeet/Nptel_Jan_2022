import string, random
bags = {}
name = string.ascii_letters
for i in range(20):
    bags[name[i]] = 0

print(bags.keys())
for i in range(1000):
    key = random.choice(list(bags.keys()))
    print(bags[key], bags[key]+1, key, end = " ")
    bags[key] = bags[key] + 1
    print(bags)