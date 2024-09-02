import random

LOWER = 1
UPPER = 1000
attempts = 0

num=random.randint(LOWER, UPPER)
guess=int(input(f"Enter a number {LOWER} - {UPPER}\n"))
if LOWER <= guess <= UPPER:
    pass
else:
    print("Not valid number.")
    quit()

while num!= guess:
    if guess < num:
        print("Too low")
        guess = int(input("Enter number again: "))
        attempts += 1
    elif guess > num:
        print("Too high!")
        guess = int(input("Enter number again: "))
        attempts += 1
    else:
      break
print(f"You guessed it right in {attempts} guesses!")
