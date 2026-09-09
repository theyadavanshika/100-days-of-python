class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_one = User("001", "Anshika") 
user_two = User("002", "Anshi")

user_one.follow(user_two)
print(user_one.following)
print(user_one.followers)
print(user_two.following)
print(user_two.followers)