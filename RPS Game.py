import random

while True:
    choices = ['rock', 'paper', 'scissors']

    com = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors : ").lower()

    if com == player:
        print("computer :", com)
        print("player   :", player)
        print("Tie")

    elif player == "paper":
        if com == "rock":
            print("computer :", com)
            print("player   :", player)
            print("u win")
        if com == "scissors":
            print("computer :", com)
            print("player   :", player)
            print("u lose")

    elif player == "rock":
        if com == "scissors":
            print("computer :", com)
            print("player   :", player)
            print("u win")
        if com == "paper":
            print("computer :", com)
            print("player   :", player)
            print("u lose")

    elif player == "scissors":
        if com == "paper":
            print("computer :", com)
            print("player   :", player)
            print("u win")
        if com == "rock":
            print("computer :", com)
            print("player   :", player)
            print("u lose")

    play_again = input("do u want to play again (yes/no) ?: ").lower()
    if play_again != "yes":
        break

print("BYE")
