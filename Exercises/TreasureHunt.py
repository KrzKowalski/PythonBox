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

first_s = input("Where do you want to go? Left or right?")

if first_s.lower() == "left":
    second_s = input("You have come at the mysterious lake. You can see a boat swimming towards you, but it is extremely slow. Do you 'swim' or 'wait' for it?")
    if second_s.lower() == "wait":
        third_s = input("The boat transported you through the lake. You have spotted a strange building with 3 doors: blue, yellow and red. Which shall you choose to open?")
        if third_s.lower() == "yellow":
            print("YOU HAVE FOUND THE TREASURE. YOU WIN!")
        elif third_s.lower() == "blue":
            print("You have been eaten by a beasts... GAME OVER.")
        elif third_s.lower() == "red":
            print("You have been burnt to death... GAME OVER.")
        else:
            print("GAME OVER.")
    else:
        print("You have been attacked by a crocodile. GAME OVER")
else:
    print("You have fallen into a hole. GAME OVER.")

