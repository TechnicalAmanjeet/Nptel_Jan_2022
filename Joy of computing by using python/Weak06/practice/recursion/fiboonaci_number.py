# implementation of fibonacci number by using recursion.

def fibo(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(20):
    print(fibo(i), end=" ")