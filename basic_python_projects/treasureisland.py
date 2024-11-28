print("Welcome to the treasure island.\nYour mission is to find the treasure.\n")
cond1 = (input("Where would you like to head towards? left or right\n")).lower()
if cond1=="left":
    cond2 = (input("Would you like to swim or wait for the boat? swim or wait?\n")).lower()
    if cond2=="wait":
        cond3 = (input("Which door would you like to choose? red, blue or yellow\n")).lower()
        if cond3=="yellow":
            print("You found the treasure! You Win!")
        elif cond3=="red":
            print("You enter a room full of dragons! Game Over!")
        else:
            print("You enter a room full of demons! Game Over!")
    else:
        print("You got attacked by a shark! Game Over!")
else:
    print("You fell into a hole! Game Over!")