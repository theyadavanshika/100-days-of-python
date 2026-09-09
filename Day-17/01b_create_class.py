class User:
    def __init__(self):
        print("New user is being created")

user_one = User()
user_one.id = "001"
user_one.username = "Anshika"

print(user_one.username)

user_two = User()
user_two.id = "002"
user_two.username = "Anshi"

print(user_two.username)


# Constructor : part of the blueprint that allows us to specify what should happen 
#               when our object being constructed