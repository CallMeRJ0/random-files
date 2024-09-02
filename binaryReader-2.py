# BIANARY READER v2

num = str(input("Select a binary number and write it like this 0 0 0 1 (MAX 8 LONG)\n"))
nums = num.split()
length = len(nums)
number = 0

def one():
    global number
    if nums[0] == "1":
        number += 1
def two():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
def three():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
def four():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
    if nums[-4] == "1":
        number += 8
def five():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
    if nums[-4] == "1":
        number += 8
    if nums[-5] == "1":
        number += 16
def six():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
    if nums[-4] == "1":
        number += 8
    if nums[-5] == "1":
        number += 16
    if nums[-6] == "1":
        number += 32
def seven():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
    if nums[-4] == "1":
        number += 8
    if nums[-5] == "1":
        number += 16
    if nums[-6] == "1":
        number += 32
    if nums[-7] == "1":
        number += 64
def eight():
    global number
    if nums[-1] == "1":
        number += 1
    if nums[-2] == "1":
        number += 2
    if nums[-3] == "1":
        number += 4
    if nums[-4] == "1":
        number += 8
    if nums[-5] == "1":
        number += 16
    if nums[-6] == "1":
        number += 32
    if nums[-7] == "1":
        number += 64
    if nums[-8] == "1":
        number += 128
def main():
        if length > 8:
            print("Too long.")
            exit()
        elif length == 1:
            one()
        elif length == 2:
            two()
        elif length == 3:
            three()
        elif length == 4:
            four()
        elif length == 5:
            five()
        elif length == 6:
            six()
        elif length == 7:
            seven()
        elif length == 8:
            eight()
main()
print("The bianary number "+str(number))
