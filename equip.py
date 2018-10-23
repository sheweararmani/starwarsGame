from player import *
from items import *


#function returns weapon if it is valid

def equip():
    templist = []
    print("Select your weapon:")
    for i in luke["inventory"]: #check to see if it is in the list
        citem = i["name"].lower()
        templist.append(citem)
    print(templist)
    while True: #loop so if the input is invalid they can try again
        weapon = input("Enter the weapon you want to equip: ").lower()
        if weapon in templist:
            return weapon
        else:
            print("Enter a valid weapon.")
