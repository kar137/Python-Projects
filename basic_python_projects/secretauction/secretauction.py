import os
from art import logo
print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("Enter your bid price: $"))
    bids[name] = bid

    choice = input("Are there any other users who wants to bid? yes or no:\n")

    if choice == "yes":
        os.system('cls')
    elif choice == "no":
        find_highest_bidder(bids)
        bidding_finished = True





