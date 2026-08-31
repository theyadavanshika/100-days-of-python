print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# use three single quotes for this type of multi block string/ascii arts

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

path = input('You\'re at a crossroad. where you wanna go? Choose a path, "left" or "right"? \n').lower()
if path == "left":
    next = input("You have come to a lake, " \
                 "there is an island in the middle of the lake," \
                 " what do you wanna do ? swim or wait?\n ")
    if next == "wait":
        Door = input("YOU ARRIVED AT THE ISLAND UNHARMED." \
                     "There's a house of 3 doors, " \
                     "select the door between Red, Blue or Yellow:\n ")
        if Door == "Red":
            print("Burned by Fire.\nGame Over!")
        elif Door == "Yellow":
            print("You found the treasure. You win!\nCongratulations")
        elif Door == "Blue":
            print("Eaten by Beast.\nGame Over!")
        else:
            print("You choose the door that dosn't exist. Game Over!")
    else:
        print("Attacted by a trout.\nGame Over!")

else:
    print("Fall into a hole.\nGame Over!")
