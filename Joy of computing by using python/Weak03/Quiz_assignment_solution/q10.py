with  open("file.txt", "w") as file:
    file.write("1000111011")
file.close()

with open('file.txt', "r") as file:
    L = list(file.read())
file.close()

print(L)
for i in range(len(L)):
    if i % 2 == 0 and L[i] == '0':
        L[i] = '1'
    if i % 2 != 0 and L[i] == '1':
        L[i] = '0'

print(L)
