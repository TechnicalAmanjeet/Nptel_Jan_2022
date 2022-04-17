def removeAdjacent(user_input):
    output = []
    for str in user_input:
        if not str in output:
            output.append(str)
    return "".join(output)

user_input = input()
output = removeAdjacent(user_input)
print(output)