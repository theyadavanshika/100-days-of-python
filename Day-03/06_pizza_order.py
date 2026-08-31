print("Welcome to python pizza deliveries!")
price = 0

size = input("What size of pizza you want? S, M or L: ")
if size == "S":
    price = 15
    print("size selected : small")
elif size == "M":
    price = 20
    print("size selected : medium")
elif size == "L":
    price = 25
    print("size selected : Large ")
else:
    print("You typed wrong input. \nTry again!")
    exit()

pepperoni = input("Do you want to have pepperoni on your pizza? yes or no: ")
if pepperoni == "yes":
    if size == "S":
        price = price + 2
        # print(f"Price for small pepperoni pizza is : ${price}")
    else:
        price = price + 3
        # print(f"Price for large OR medium pepperoni pizza is : ${price}")

extra_cheese = input("Do you want extra cheese on your pizza? yes or no: ")
if extra_cheese == "yes":
    price = price + 1
    # print(f"price for cheese pizza is : {price}")

print(f"Your total price is : ${price}")   