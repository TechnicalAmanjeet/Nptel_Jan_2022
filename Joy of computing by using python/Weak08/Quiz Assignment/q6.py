import random
import matplotlib.pyplot as plt

l = []
count = 0

for i in range(10):
    gauss = random.randint(1, 10)
    pick = random.randint(1, 10)
    print(gauss, pick)

    if gauss != pick:
        count += 1
        l.append(count)
    else:
        count -= 1
        l.append(count)

plt.plot()
plt.show()