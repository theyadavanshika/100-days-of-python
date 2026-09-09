class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_one = User("001", "Anshika")
user_two = User("002", "Anshi")
print(user_two.followers)
 

# "Constructors" or "initilizing an object"
# self.id = attribute that is associated with the class User