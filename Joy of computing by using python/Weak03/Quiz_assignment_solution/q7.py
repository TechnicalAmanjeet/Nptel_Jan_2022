a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

while (1):
    if (a%b == 0):
        print("wow!")
        break
    else:
        print("if you want to continue press 1 else 0")
        choice = int(input())
        
        if choice == 1:
            b = int(input("Enter second number again : "))

        if choice == 0:
            break