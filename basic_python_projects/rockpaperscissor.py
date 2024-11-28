import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

items = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if choice>=3 or choice<0:
    print("You typed an invalid number. You lose!")
else:
    print(items[choice])

comp_choice = random.choice(items)
print(f"computer choice: {comp_choice}")
if choice==0 and comp_choice==rock:
    print("Draw")
elif choice==0 and comp_choice==scissors:
    print("You win")
elif choice==0 and comp_choice==paper:
    print("You lose")
elif choice==1 and comp_choice==paper:
    print("Draw")
elif choice==1 and comp_choice==rock:
    print("You win")
elif choice==1 and comp_choice==scissors:
    print("You lose")
elif choice==2 and comp_choice==paper:
    print("You win")
elif choice==2 and comp_choice==rock:
    print("You lose")
elif choice==2 and comp_choice==scissors:
    print("Draw")
else:
    print("You enter an invalid number. So you lose!")


