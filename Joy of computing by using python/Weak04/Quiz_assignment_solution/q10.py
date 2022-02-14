def perfect_number(num):
    output = 0
    for i in range(1, num):
        if num % i == 0 :
            output += i
    
    if output == num:
        print(f"perfect number : {num}")
    # else:
    #     print("not a perfect number")

for i in range(1, 1000):
    perfect_number(i)

        