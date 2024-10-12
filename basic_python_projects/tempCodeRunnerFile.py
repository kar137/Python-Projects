row1= ["⬜", "⬜", "⬜"]
row2= ["⬜", "⬜", "⬜"]
row3= ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
if position=="31":
    row1[2]="💰"
    
print(f"{row1}\n{row2}\n{row3}")