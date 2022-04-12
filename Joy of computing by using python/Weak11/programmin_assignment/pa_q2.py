str = input()
list = list(str.split("#"))
list.sort(reverse=True)

for i in range(len(list)):
    print(list[i], end="")
    if i != len(list)-1:
        print("#", end="")