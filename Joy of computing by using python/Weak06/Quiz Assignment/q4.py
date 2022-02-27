def recursive(num):
    if num == 1 : return 1
    return num * (num-1)

def sum(num):
    s = 0
    for i in range(num+1):
        s += i
    return s

print(recursive(9))
print(sum(9))