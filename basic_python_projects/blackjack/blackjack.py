
import random

def deal_card():
    """Return a random number corresponding to a card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def sum(card_list):
    total = 0
    for item in card_list:
        total += item
    return total

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You Lose! Opponent has blackjack."
    elif user_score == 0:
        return "You Win! You got blackjack."
    elif user_score > 21:
        return "You went over. You Lose!"
    elif computer_score > 21:
        return "Opponent went over. You Win!"
    elif user_score > computer_score: 
        return "You Win!"
    else:
        return "You Lose!"

def playgame():
    from art import logo
    print(logo)
    your_cards = []
    computer_cards = []
   
    for _ in range(2):
        your_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    
    is_game_over = False

    while not is_game_over:
        user_score = calc_score(your_cards)
        computer_score = calc_score(computer_cards)

        print(f"\nYour_cards: {your_cards}, Current_score: {user_score}")
        print(f"Computer's first_card: {computer_cards[0]}\n")
        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True

        else:
            choice2 = input("Type 'y' to get another card or Type 'n' to pass: ")
            if choice2 == 'y':
                your_cards.append(deal_card())
            elif choice2 == 'n':
                is_game_over = True
    while computer_score!=0 and computer_score <= 16:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print(f"\nYour final hand: {your_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score=user_score, computer_score=computer_score))

while input("\nDo you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    import os
    os.system('cls')
    playgame()

    
        


