import random

print('''Welcome to "Rock Paper and Scissor Game" ''')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissor]

you_choose = input("What do you wanna choose?\n" \
                   "Press 0 for Rock, 1 for Paper and 2 for Scissor :")

if you_choose == "0":
    print(rock)
elif you_choose == "1":
    print(paper)
elif you_choose == "2":
    print(scissor)
else:
    print("You enetered something wrong.\nTry Again!")
    exit()

computer_choose = random.randint(0,2)
print(options[computer_choose])

if computer_choose == 0 and you_choose == "0":
    print("It's a Draw")
elif computer_choose == 1 and you_choose == "1":
    print("It's a Draw")
elif computer_choose == 2 and you_choose == "2":
    print("It's a Draw")
    
elif computer_choose == 0 and you_choose == "1":
    print("You win!")
   
elif computer_choose == 1 and you_choose == "0":
    print("You lost!")

elif computer_choose == 0 and you_choose == "2":
    print("You win!")

elif computer_choose == 2 and you_choose == "0":
    print("You lost!")

elif computer_choose == 1 and you_choose == "2":
    print("You win!")

elif computer_choose == 2 and you_choose == "1":
    print("You loose!")

else:
    print("Something went wrong")

print("Thankyou for playing the game.")