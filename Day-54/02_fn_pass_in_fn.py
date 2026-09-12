def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2 

#Functions are first class objects, can be passed around as arguments eg: int/string/float etc.
def calculate(cal_function, n1, n2):
    return cal_function(n1,n2)
result = calculate(add, 2, 3)
print(f"addition = {result}")  