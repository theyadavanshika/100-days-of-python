print("welcome to the rollercoaster!")
height = int(input("Enter the height in cm: "))
bill = 0

if height >= 120:
    print("you can ride a rollercoaster")
    age = int(input("Enter your age: "))
    if age <=12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 18
        print("Teen tickets are $7")
    else:
        bill = 20
        print("Adult tickets are $20")

    want_photos = input("Do you want to have a photograph? type yes or no :")
    if want_photos == "yes":
        #Add $3 to the bill
        bill = bill + 3

    print(f"Your final bill is ${bill}")
else:
    print("you can't ride a rollercoaster")