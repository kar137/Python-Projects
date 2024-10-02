import random
random_int = random.randint(0,1)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

#list

state1="pennyslvania"
state2="texas"

states_of_america = ["Texas","Washington","Chicago"]

state = states_of_america[2]
states_of_america[2] = "Las vegas"

states_of_america.append("Martianland")
states_of_america.extend(["Texaland","herbiland"])
print(states_of_america)
