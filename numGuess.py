import random

print("Number guessing game!")

nrange=int(input("Pick the highest range for a number to guess:\n"))
number = random.randint(1, nrange)
print(number)
guess = int(input(f"Guess a number 1 - {nrange}:\n"))
if guess == number:
    print("You guessed if correctly!")
    repeat=int(input("You would you like to guess again? | 1 to start game | 2 to exit program |"))
    if repeat == 1:
        print("ERROR")
        exit()
    elif repeat == 2:
        exit()
    else:
        exit()
elif guess != number:
    if number > guess:
        print(f"The number is higher than {guess}")
        
        while guess != number:
            guess = int(input(f"Guess a number 1 - {nrange}:\n"))
            
            
    elif number < guess:
        print(f"The number is lower than {guess}")
        
        while guess != number:
            guess = int(input(f"Guess a number 1 - {nrange}:\n"))
            
"""
This didn't work since I couldn't rerun the guessing since I didnt make it a function
Im going to try again but with different functions I can use to run different parts of the game.
"""
