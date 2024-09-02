# BIANARY READER V1

number = 0
bianary = str(input("Type in a bianary number written like \"0 0 0 0 0 1\" 6 charcters long."))
print(bianary)
nums = bianary.split()

if nums[0] == "1":
    number += 32
if nums[1] == "1":
    number += 16
if nums[2] == "1":
    number += 8
if nums[3] == "1":
    number += 4
if nums[4] == "1":
    number += 2
if nums[5] == "1":
    number += 1
print(number)
