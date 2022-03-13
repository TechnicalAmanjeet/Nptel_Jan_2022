def snake(M):
    output = []
    for i in range(len(M)):
        if i % 2 == 0:
            for j in range(len(M[i])):
                output.append(M[i][j])
        else:
            length = len(M[i])
            for j in range(len(M[i])):
                output.append(M[i][length-j-1])
    return output
