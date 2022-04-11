# program for lottary simulation.
import random
import time

accounts = 0
times = 10

for itr in range(times):
    # user_bet = int(input("Enter your bet ( b/w 1-10 ) : "))
    user_bet = random.randint(1,10)
    # time.sleep(0.01)
    random_bet = random.randint(1, 10)

    if user_bet == random_bet:
        print(itr)
        accounts = accounts + 900
    else:
        accounts -= 100
    # print(f"Actual bet : {random_bet}")
    # print(f"Your balance : {accounts}")

print(accounts)