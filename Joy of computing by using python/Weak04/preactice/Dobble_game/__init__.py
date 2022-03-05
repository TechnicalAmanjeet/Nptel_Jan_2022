# dobble game.

import string
import random

# symbol = list(string.ascii_letters)
symbol = list(string.ascii_lowercase)
# for i in range(10):
#     symbol.append(i)
# print(symbol)

card1 = [0]*8
card2 = [0]*8

position1 = list(range(8))
position2 = list(range(8))

pos1 = random.choice(position1)
position1.remove(pos1)
pos2 = random.choice(position2)
position2.remove(pos2)
# print(symbol,card1, card2)

samesymbol = random.choice(symbol)
symbol.remove(samesymbol)

answer = samesymbol

if pos1 == pos2:
    card1[pos1] = samesymbol
    card2[pos1] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol

    card1[pos2] = random.choice(symbol)
    symbol.remove(card1[pos2])

    card2[pos1] = random.choice(symbol)
    symbol.remove(card2[pos1])

while len(position1) != 0:
    pos1 = random.choice(position1)
    position1.remove(pos1)
    pos2 = random.choice(position2)
    position2.remove(pos2)

    card1[pos1] = random.choice(symbol)
    symbol.remove(card1[pos1])
    card2[pos2] = random.choice(symbol)
    symbol.remove(card2[pos2])

print(card1)
print(card2)
print(answer)
print(position1)
print(position2)
print(symbol)
