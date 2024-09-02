# Rolling dice simulator V2

import random

total_rolls = int(input("Select how many rolls you would like to roll (MAX 1000): "))
if total_rolls > 1000 or total_rolls < 1:
    print("Incorrect number of rolls try again.")
    exit()
numbers = []
while total_rolls != 0:
    numbers.append(random.randint(1,6))
    total_rolls -= 1

one = numbers.count(1)
two = numbers.count(2)
three = numbers.count(3)
four = numbers.count(4)
five = numbers.count(5)
six = numbers.count(6)

print(f"There are {one} 1\nThere are {two} 2\nThere are {three} 3\nThere are {four} 4\nThere are {five} 5\nThere are {six} 6")
