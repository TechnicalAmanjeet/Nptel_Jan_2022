def replaceV(S):
    vovel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = S

    for i in range(len(S)-2):
        if S[i] in vovel and S[i+1] in vovel and S[i+2] in vovel:
            a = a.replace(S[i]+S[i+1]+S[i+2], "_")

    return a


S = input()
print(replaceV(S))