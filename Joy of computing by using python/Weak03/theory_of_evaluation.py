# will open text file and read write data of it.

# modes of file by which we can open any file.
# 1. "r" => read only mode
# 2. "w" => write only mode override the data.
# 3. "a" => write only mode but append the data at the end.
# 4. "r+" => can perform both read and write operations.

with open("file.txt", mode="r") as file:  # 1st mode
    print(file.read())

# 2nd mode
with open("file.txt", "w") as file:
    file.write("Amanjeet loves riya")

with open("file.txt", mode="r") as file:  # 1st mode
    print(file.read())
    
with open("file.txt", "a") as file:  # 3rd mode
    file.write("\ndon't know about others")

with open("file.txt", mode="r") as file:  # 1st mode
    print(file.read())

with open("file.txt", "r+") as file:  # 4th mode
    file.write("\nBut i love her from bottom of my heart.")
    print(file.read())
