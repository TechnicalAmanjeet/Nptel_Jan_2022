def recursive(num):
    if num == 1:
        print("*")
        return

    elif num % 2 == 0:
        print("*" * num)
        recursive(num-1)
        return

    else:
        recursive(num-1)
        return
recursive(10)