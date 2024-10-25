with open("../../../OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode= "a") as file:
    file.write("\nI am currently studying.")
