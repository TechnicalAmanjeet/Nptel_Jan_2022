import time
n = 10

for i in range(n):
    if i % 2 == 0:
        temp = n*i + 1
        t = n;
        while(t>0):
            time.sleep(0.5)
            print(temp, end=" ")
            temp += 1
            t -= 1
        print()
    else:
        temp = n*i + 1
        t = n;
        while t > 0:
            time.sleep(0.5)
            print(temp, end=" ")
            temp += 1
            t -= 1
        print()
