print("welcome to the rollercoaster!")
height = int(input("Enter the height in cm: "))

if height >= 120:
    print("you can ride a rollercoaster")
    age = int(input("Enter your age: "))
    if age <=12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $20")
else:
    print("you can't ride a rollercoaster")