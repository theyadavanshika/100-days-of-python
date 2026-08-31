print("Welcome to the tip calculator!")

totalbill = input("What was the total bill? $")

b = int(totalbill)

tip = input("How much tip would you like to give? 10, 12 or 15% ")

a = int(tip)
money = b + (b * (a/100))

people = int(input("How many people to split the bill? "))

payment = money/people
print("Each person should pay: ", round(payment, 2))
print(f"Each person should pay ${round(payment,2)} ")
