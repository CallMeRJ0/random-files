import random

AI_reset=False
Self_reset=False

temp=int(input("Whould you like to play 2 player or one player? | 1 for 1 player | 2 for 2 player:\n"))
if temp <1 or temp > 2:
    print("Please select a valid input.")
    exit()
print("\n" * 2)

def AI():
    print("\n" * 2)
    AI_reset=False
    Player_Choice = int(input("1 for Rock | 2 for Paper | 3 for Scissors"))
    if Player_Choice <1  or Player_Choice > 3:
        print("That is an invalid input.")
        print("\n")
        AI_reset=True
        return

    AI_Choice=random.randint(1,3)
    if Player_Choice == AI_Choice:
        win_state="You tied!"
    if (Player_Choice == 1 and AI_Choice == 2) or (Player_Choice == 2 and AI_Choice == 3) or (Player_Choice == 3 and AI_Choice == 1):
        win_state="You lose!"
    if (Player_Choice == 1 and AI_Choice == 3) or (Player_Choice == 2 and AI_Choice == 1) or (Player_Choice == 3 and AI_Choice == 2):
        win_state="You win!"
       
    if Player_Choice == 1:
        Player_Choice = "Rock"
    elif Player_Choice == 2:
        Player_Choice = "Paper"
    elif Player_Choice == 3:
        Player_Choice = "Scissors"
           
    if AI_Choice == 1:
        AI_Choice = "Rock"
    elif AI_Choice == 2:
        AI_Choice = "Paper"
    elif AI_Choice == 3:
        AI_Choice = "Scissors"
    print("You picked " + Player_Choice + " and Python picked " + AI_Choice + " that means, " + win_state)
    print("\n")
    AI_reset=True
    return

def Self():
    print("\n" * 2)
    Self_reset=False
    Player_Choice1 = int(input("1 for Rock | 2 for Paper | 3 for Scissors (Player 1)"))
    print("\n" * 100)
    Player_Choice2 = int(input("1 for Rock | 2 for Paper | 3 for Scissors (Player 2)"))
    if (Player_Choice1 < 1  or Player_Choice1 > 3) or (Player_Choice2 < 1 or Player_Choice2 > 3):
        print("A player made a invalid choice.")
        exit()
    if Player_Choice1 == Player_Choice2:
        win_state="it was a tie!"
    if (Player_Choice1 == 1 and Player_Choice2 == 2) or (Player_Choice1 == 2 and Player_Choice2 == 3) or (Player_Choice1 == 3 and Player_Choice2 == 1):
        win_state="Player two wins!"
        p2_points = 0
        p2_points+=1

    if (Player_Choice1 == 1 and Player_Choice2 == 3) or (Player_Choice1 == 2 and Player_Choice2 == 1) or (Player_Choice1 == 3 and Player_Choice2 == 2):
        win_state="Player one wins!"
        p1_points = 0
        p1_points+=1

    if Player_Choice1 == 1:
        Player_Choice1 = "Rock"
    elif Player_Choice1 == 2:
        Player_Choice1 = "Paper"
    elif Player_Choice1 == 3:
        Player_Choice1 = "Scissors"
           
    if Player_Choice2 == 1:
        Player_Choice2 = "Rock"
    elif Player_Choice2 == 2:
        Player_Choice2 = "Paper"
    elif Player_Choice2 == 3:
        Player_Choice2 = "Scissors"
    print(f"Player one picked {Player_Choice1} and player two picked {Player_Choice2} that means, {win_state}")
    p1_win = 0
    p2_win = 0
    if p1_win==1:
        print(f"Player one has {p1_points} points.")
        p1_win=0
    if p2_win==1:
        print(f"Player two has {p2_points} points.")
        p2_win=0
    if p2_win and p1_win == 0:
        print("placeholder")
    Self_reset=True
    return

if temp == 1:
    AI_reset=True
    AI()
if temp == 2:
    Self_reset=True
    Self()
while True:
    if AI_reset==True:
        AI()
    if Self_reset==True:
        Self()
