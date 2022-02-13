with open("file.txt", "r") as file:
    print(file.read())
    file.write("hay there!")
file.close()