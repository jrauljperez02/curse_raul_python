print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("Left or right? ")
choice.lower()
if choice == "right":
    print("Fall into a hole")
    print("GAME OVER")
elif choice == "left":
    choice = input("Swim or wait a boat? ")
    choice.lower()
    if choice == "swim":
        print("Attacked by trout")
        print("GAME OVER")
    elif choice == "wait":
        print("You arrived to an island")
        print("There are some differnt door's colors,select one")
        choice = input("RED - YELLOW - BLUE - GREEN ")
        choice.lower()
        if choice == "red":
            print("Burned by fire")
            print("GAME OVER")
        elif choice == "yellow":
            print("YOU WIN!")
            print("CONGRATULATIONS")
        elif choice == "blue":
            print("Eaten by beasts")
            print("GAME OVER")
        elif choice == "green":
            print("Something has bite you")
            print("GAME OVER")
