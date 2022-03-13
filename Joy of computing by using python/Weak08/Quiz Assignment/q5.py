print("Enter a letter between a-z : ")

player1 = str(input())
player2 = str(input())

while True:
    if ord(player1.lower())+1 == ord(player2.lower()):
        print("Clap")
        break
    else:
        player1 = str(input())
        player2 = str(input())