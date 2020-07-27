"""Rock, paper scissor"""

from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer= t[randint(0,2)]

#set player to False
player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win", player, "rocks", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "wins against", player)
        else:
            print("You win!", player, "blankets", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "rocks" , player)
        else:
            print("You win!", player,"wins against", computer)
    else:
        print("this isn't valid, spell check")

    player = False
    computer = t[randint(0,2)]
