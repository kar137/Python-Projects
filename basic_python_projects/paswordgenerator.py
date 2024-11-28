import random
import string

letters = list(string.ascii_letters)
digits = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["@","#","$","%","!","*","(",")","^","_",">"]

print("Welcome to the PyPassword Generator:")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

pw_letter = ""
pw_symbol = ""
pw_number = ""

for n in range(0, nr_letters):
    pw_letter+=random.choice(letters)
for n in range(0, nr_symbols):
    pw_symbol+=random.choice(symbols)
for n in range(0, nr_numbers):
    pw_number+=random.choice(digits)

pw_list= list(pw_letter+pw_number+pw_symbol)

random.shuffle(pw_list)
password=""
for char in pw_list:
    password+=char

print(f"Your generated password is {password}")

