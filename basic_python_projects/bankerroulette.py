import random
name_string = input("Give me everbody's names, separated by a comma.\n")
names = name_string.split(",")
print(names)
x=len(names)

random_name = names[random.randint(0,x-1)]
print(f"{random_name} is going to buy the meal today")