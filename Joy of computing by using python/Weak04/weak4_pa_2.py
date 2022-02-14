s = input("Enter a string: ")
vovel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
output = ""

for ch in s:
    if ch not in vovel:
        output += "_"
    else:
        output += ch
print(output)
