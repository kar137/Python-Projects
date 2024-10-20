class User:
    #pass  ->this just passes the command to the next line of code
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Jack")
user_2 = User("002", "Karen")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

user_2.follow(user_1)
print(user_2.followers)
print(user_2.following)