import random
import os
from art import logo
print(logo)

from game_data import data
id_1 = random.choice(data)
id_2 = random.choice(data)

count = 0

def game(id_1, id_2):
    global count
    print(f"Compare A: {id_1["name"]}, a {id_1["description"]}, from {id_1["country"]}.")

    from art import vs
    print(vs)

    print(f"Against B: {id_2["name"]}, a {id_2["description"]}, from {id_2["country"]}.")

    choice = (input("Who has more followers?Type A or B: ")).lower()
    if choice == "a" and id_1["follower_count"] >= id_2["follower_count"] or choice == "b" and id_2["follower_count"] >= id_1["follower_count"]:
        count += 1
        os.system('cls')
        print(f"You guessed correct. Your current score = {count}")
        game(id_2 , id_2 = random.choice(data))
        
    else:
        os.system('cls')
        print(f"You guessed wrong. Your final score = {count}")

game(id_1=id_1, id_2=id_2)
    



