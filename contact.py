#contacts list
"""
contacts = {}
def main():
    temp=int(input("Type 1 to view contacts or 2 to add a new contact.\n"))
   
   
    def addcontact():
        tempNum = int(input("Please type their Phone Number: "))
        tempName = str(input("Type their contact name: "))
        contacts[tempName] = tempNum
        print("Contact added : " + '\n'.join("{} | {}".format(k, v) for k, v in contacts.items()))
        print("\n"*3)
   
    def viewcontacts():
        print("" + '\n'.join("{}".format(k, v) for k, v in contacts.items()
        tempStore = str(input("Type in a persons name to see their number or type 1 to go to main menu: "))
        if tempStore == 1:
            print("\n"*3)
        else:
            print(f"{tempStore}'s number is {contacts.get(tempStore)}")
    if temp == 1:
        viewcontacts()
    if temp == 2:
        addcontact()
    if temp > 2 or temp < 1:
        print("Error")
while True:
    main()
"""
