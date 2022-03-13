word = "facebook"
new = ""

for w in word:
    i = ord(w)
    j = (((i+26) - 97) % 26) + 97
    new = new + chr(j)

print(new)