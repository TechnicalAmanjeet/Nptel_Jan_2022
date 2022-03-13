
def squareT(T):
    m = []
    for w in T:
        m.append(w)
    for w in T:
        m.append(w*w)
    return tuple(m)

if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    T = tuple(L)
    ans = squareT(T)
    if type(ans) == type(T):
        print(ans)