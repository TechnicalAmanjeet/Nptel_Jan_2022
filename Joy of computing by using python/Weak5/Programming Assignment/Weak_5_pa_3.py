L = [int(i) for i in input().split()]

def isprime(n):
    # Corner case
    if n <= 1:
        return False

    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;

    return True

for element in L:
    if isprime(element):
        print(element)
        break