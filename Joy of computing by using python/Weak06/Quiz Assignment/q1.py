import string


def shift(word, value):
    letters = string.ascii_lowercase
    new = ''

    for i in range(len(word)):
        if word[i] in letters:
            index = letters.index(word[i])
            new = new + letters[(index + value) % 26]
        else:
            new = new + word[i]

    return new

print((shift("Amanjeet", 10)))
