print("Welcome to the tip calculator:\n")

bill_amt = input("What's your total bill? $")


per = input("What percentage tip would you like to give? 10, 12 or 15 ")

num = input("How many people to split the bill? ")

total_amt = float(bill_amt) + (float(bill_amt) * float(per))/100
individual_amt = total_amt/int(num)
final_amt1 = round(individual_amt)  #if there is 33.60 then it gives 33.6
final_amt2= "{:.2f}".format(individual_amt) #it gives 33.60
print(f"Each person should pay: ${final_amt2}")