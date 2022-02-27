

# ******** code to copy start ********

def whole(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + whole(n-1)

# ******* code to copy end ********


N = int(input())
print(whole(N))