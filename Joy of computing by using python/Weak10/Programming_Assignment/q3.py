str = input()

for s in str:
    if s == " ":
        print(s, end="")
    elif ord(s) >= ord('a') and ord(s) <= ord('z'):
        print(s.upper(), end="")
    else:
        print(s.lower(), end="")