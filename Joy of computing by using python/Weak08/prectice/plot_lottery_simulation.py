# program for lottary simulation.
import random
import matplotlib.pyplot as plt
import time

accounts = 0
times = 365
x = []
y = []


for itr in range(times):
    # user_bet = int(input("Enter your bet ( b/w 1-10 ) : "))
    user_bet = random.randint(1,10)
    # time.sleep(0.01)
    random_bet = random.randint(1, 10)

    if user_bet == random_bet:
        # print(itr)
        accounts = accounts + 900
    else:
        accounts -= 100
    x.append(itr)
    y.append(accounts)
    # print(f"Actual bet : {random_bet}")
    # print(f"Your balance : {accounts}")

# print(accounts)
# print(x)
# print(y)
plt.plot(x, y)
plt.show()