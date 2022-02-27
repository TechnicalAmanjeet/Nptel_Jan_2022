d = {0:"rock", 1:"paper", 2:"scissors"}
# choice = int(input())
for choice in range(15):
    game_choice = d[choice % 3]
    print(game_choice)