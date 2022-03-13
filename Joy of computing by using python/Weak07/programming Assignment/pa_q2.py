import numpy
from array import *

def Transpose(M):
    arr = numpy.array(M)
    num_list = arr.transpose().tolist()

    return num_list




# n = int(input())
# M = []
# for i in range(n):
#     L = list(map(int, input().split()))
#     M.append(L)
# print(Transpose([[51, 100, 90], [81, 18, 59], [52, 2, 58]]))

p = [[51, 100, 90], [81, 18, 59, 12, 14], [52, 2, 58]]
print(len(p[0]))
print(len(p[1]))
print(len(p[2]))

