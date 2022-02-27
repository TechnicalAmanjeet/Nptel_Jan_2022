# weak 6 programming Assignment : 1

N = int(input())
L = [int(i) for i in input().split()]
K = int(input())

# ******** code to copy start ********

fav_plant_dis = L[K-1]
L.sort()
print(L.index(fav_plant_dis) + 1)

# ******* code to copy end ********
