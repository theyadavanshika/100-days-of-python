import random
friends = [ "Anshika", "Ankush", "Bob", "Alice", "Angelina", "David"]

# option 1
print(random.choice(friends))

#2nd option
random_index = random.randint(0,4)
print(friends[random_index])

