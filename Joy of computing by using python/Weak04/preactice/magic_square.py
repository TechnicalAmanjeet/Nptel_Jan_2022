# Megic Square

# for 3 * 3 matrix
#  2  7  6
#  9  5  1
#  4  3  8

# for 5 * 5 matrix
#   9  3  22  16  15
#   2 21  20  14  8
#  25 19  14   7  1
#  18 12   2   6  24
#  11 10   4  23  17

# some facts for making this magic square.
# sum = (n * ( n^2 + 1 ))/ 2

# steps :
# 1. in any megic square, 1 will always be located at ( n/2 , n-1 ).

# 2. let's say the position of 1 i.e ( n/2 , n-1 ) is (p,q), then the next number which is 2 is located
#    at ( p-1 , q+1 ).
#   anytime if the calculated row positon becomes -1 then make it n-1 and if column position becomes n then
#   make it 0.

# 3. if the calculated position already contains a number then the decrement the column by 2 and increment row by 1
#    if anytime row position becomes -1 and columns becomes n, switch it to (0, n-2).

magic_square3 = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

# for i in range(3):
#     for j in range(3):
#         magic_square[i][j] = i * j;

# print("welcome to " , end=' ')

def show():
    for i in range(3):
        print("   ", end=" ")
        for j in range(3):
            print(str(magic_square3[i][j]), end="   ")
        print()


# implementing magic square matrix.
n = 3  # order of matrix
# position for 1.
r = n//2  # will follow the row.
c = n-1  # will follow the c.
decrement_coulmn = 1
increment_row = 1

order = 1
max_order = n*n + 1;

while order != max_order:
    print(r, " ", c, " ", order)
    magic_square3[r][c] = order
    order += 1

    r = r-1
    c = c+1

    if r <= -1:
        r = n-1
    if c >= n:
        c = 0

    if magic_square3[r][c] != 0:
        r = r+1
        c = c-2

        if r== n and c<= -1:
            r= 0
            c= n-2

        if r <= -1:
            r = 0

        if c >= n:
            c = n-2









show()



# show()



