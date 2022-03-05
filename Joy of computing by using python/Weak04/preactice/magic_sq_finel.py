magic_square = []


def magic_sq(n):
    global magic_square
    magic_square = [[0 for i in range(n)] for j in range(n)]
    # print(magic_square)
    r = n//2
    c = n-1
    order = 1
    max_order = n*n + 1

    while order != max_order:
        if r == -1 and c == n:
            r = 0
            c = n - 2
        else:
            if c==n:
                c = 0
            if r < 0:
                r = n-1

        # print(r, " " , c)

        if magic_square[r][c] != 0:
            r = r+1
            c = c-2
            continue
        else:
            magic_square[r][c] = order
            order += 1

        r = r-1
        c = c+1


def show(n):
    for i in range(n):
        for j in range(n):
            print(magic_square[i][j], end="  ")
        print()


N = 11  # size of magic square.
magic_sq(N)  # Build the magic sq.
show(N)  # print magic square in matrix form.
