def spiral(row, col, arr):
    rs = 0
    cs = 0

    while rs < row and cs < col:
        for i in range(rs, row):
            print(arr[i][cs], end=" ")
        cs = cs + 1

        for i in range(cs, col):
            print(arr[row-1][i], end=" ")
        row = row - 1

        if rs < row:
            for i in range(row-1, rs-1, -1):
                print(arr[i][col-1], end=" ")
            col = col - 1

        if cs < col:
            for i in range(col-1, cs-1, -1):
                print(arr[rs][i], end=" ")

            rs = rs + 1

matrix = [[1, 2, 3],
          [5, 6, 7],
          [9, 10, 11]]

row = 3
col = 3
spiral(row, col, matrix)
