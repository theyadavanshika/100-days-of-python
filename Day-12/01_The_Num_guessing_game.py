import random
import art

print(art.design)
print("Welcome to the Number Guessing Game!\n")

difficulty = input("I'm thinking of a number between 1 and 100.\nChoose the difficulty. Type 'easy' or 'hard' : ").lower()
correct_number = random.randint(1,100)
if difficulty == "easy":
    for attempts in range(1,11):
        guess_number = int(input("Guess your number :"))
        if guess_number == correct_number:
            print(f"You guessesd the correct number. {guess_number}")
            break
        elif guess_number != correct_number:
            print(f"YOU HAVE {10 - attempts} LEFT")
            if attempts == 10:
                print("Sorry, You lose!")
                break
            if guess_number > correct_number:
                print("Too high, Guess again")
            elif guess_number < correct_number:
                print("Too low, Guess again")
            

elif difficulty == "hard":
    for attempts in range(1,6):
        guess_number = int(input("Guess your number :"))
        if guess_number == correct_number:
            print(f"You guessesd the correct number : {guess_number}")
            break
        elif guess_number != correct_number:
            print(f"YOU HAVE {5 - attempts} LEFT")
            if attempts == 5:
                print("Sorry, You lose!")
                break
            elif guess_number > correct_number:
                print("Too high, Guess again")
            elif guess_number < correct_number:
                print("Too low, Guess again")
            


