import art
print(art.logo)

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add, 
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
n1 = int(input("What's your first number?: "))
while True:
    print("+\n-\n*\n/")
    pick = input("pick an operation: ")
    n2 = int(input("What's your next number?: "))
    if pick == "+":
            result = operations["+"](n1,n2)
    elif pick == "-":
            result = operations["-"](n1,n2)
    elif pick == "*":
            result = operations["*"](n1,n2)
    elif pick == "/":
            result = operations["/"](n1,n2)

    print(f"{n1} {pick} {n2} : {result}")
    proceed = input(f"Do you want to continue working with the previous result?\ntype 'yes' for continue calculating with {result} or 'no' :  ")
    if proceed == "yes":
        n1 = result
        continue
    if proceed == "no":
        print("ThankYou")
        break

    
        
        
            






    

