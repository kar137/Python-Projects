import random

from hangman_words import word_list
from hangman_art import logo, stages
lives = 6
chosen_word = random.choice(word_list)
print(f"The solution is: {chosen_word}")

display = []
n = len(chosen_word)

for _ in range(n):
    display.append("_") 
print(display)
end_of_game=False
while not end_of_game:
    guess = (input("Guess a letter in the word?\n")).lower()
    if guess in display:
         print("You have alredy guessed this character.")
    for position in range(n):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
          print(f"Your guess {guess} is not in the word. You lose a life!")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose!")
        

    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print (stages[lives])