start = int(input())
last = int(input())

def isprime(num):
    if num < 4:
        return True
    counter = 2
    while(counter <= num//2):
        if num % counter == 0:
            return False
        counter += 1
    return True

for num in range(start, last+1):
    # print(num, end=" ")
    if not isprime(num):
        print(num)
    # print()