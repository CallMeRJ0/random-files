print("We are going to calcuate the % you got on your test.")
total_marks = int(input("How many questions were there in total: "))
test_type = str(input("What type of test was it: "))
mark = int(input("and how many did you get right: "))
if mark > total_marks:
    print("Try again, your score was higher than the total marks.")
    exit()
percent = (mark/total_marks)*100
percent = round(percent, 3)
print(f"You got {percent}% out of 100% on your {test_type} test.")
