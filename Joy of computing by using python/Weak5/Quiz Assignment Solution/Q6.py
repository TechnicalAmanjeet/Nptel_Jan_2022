import string

bags = {}
name = string.ascii_letters
for i in range(20):
    bags[name[i]] = 0

print(bags)