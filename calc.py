input1=float(input("Select your first input:\n"))
input2=float(input("Select your second input:\n"))
type=int(input("What function would you like to run? | 1 for + | 2 for - | 3 for x | 4 for / |\n"))

def add():
    print(f"{input1} + {input2} = {float(input1)+float(input2)}")
    return
def take():
    print(f"{input1} - {input2} = {float(input1)-float(input2)}")
    return
def mul():
    print(f"{input1} * {input2} = {float(input1)*float(input2)}")
    return
def div():
    print(f"{input1} / {input2} = {float(input1)/float(input2)}")
    return
if type == 1:
    add()
elif type == 2:
    take()
elif type == 3:
    mul()
elif type == 4:
    div()
else:
    print("Error")
    quit()
