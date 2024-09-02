start=True
win=1
import random

def main():
    start=False
    numchoice=int(input("Pick a number 1 - 3 (1 for Rock : 2 for Paper : 3 for Scissors): \n"))
    while numchoice > 3 or numchoice < 1:
        if numchoice > 3 or numchoice < 1:
            print("You choice is not between 1 and 3, plase select a valid number.")
            numchoice=int(input("Pick a number 1 - 10: \n"))
    AI_numchoice = random.randint(1 , 3)

    if numchoice == AI_numchoice:
        print("Tie!")
        win=3
    elif  (numchoice == 1 and AI_numchoice == 2) or (numchoice == 2 and AI_numchoice == 3) or (numchoice == 3 and AI_numchoice == 1):
        print("You lose!")
        win=0
    elif  numchoice == 1 and AI_numchoice == 3:
        print("You win!")
        win=1
    elif  numchoice == 2 and AI_numchoice == 1:
        print("You win!")
        win=1
    elif  numchoice == 2 and AI_numchoice == 3:
        print("You lose!")
        win=0
    elif  numchoice == 3 and AI_numchoice == 2:
        print("You win!")
        win=1

    if numchoice == 1:
        numchoice = "Rock"
    if numchoice == 2:
        numchoice = "Paper"
    if numchoice == 3:
        numchoice = "Scissors"
    if AI_numchoice == 1:
        AI_numchoice = "Rock"
    if AI_numchoice == 2:
        AI_numchoice = "Paper"
    if AI_numchoice == 3:
        AI_numchoice = "Scissors"
    if win == 1:
        win = "You win!"
    if win == 0:
        win = "You lose!"
    if win == 3:
        win = "You tied!"
    print("You picked " + str(numchoice) + " and Python picked, " + str(AI_numchoice) + " that means " + str(win))
    start=True
while True:
    if start == True:
        main()
