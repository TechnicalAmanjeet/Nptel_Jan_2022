import string

def test(word):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    new = ''

    for ch in word:
        if ch in lower:
            index = lower.index(ch)
            new += lower[(index + 2) % 26]

        elif ch in upper:
            index = upper.index(ch)
            new += upper[(index + 3) % 26]

        else:
            new += ch

    return new

print(test("The Joy OF Computing"))