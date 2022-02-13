with open("file.txt", "w") as file:
    file.write("hey there!!")
file.close()

with open("file.txt", "a") as file:
    file.write("writing this file again")
file.close()

with  open("file.txt", "r") as file:
    print(file.read())