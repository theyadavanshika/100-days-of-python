def calculate(**kwargs): #unlimited keywords arguments
    print(kwargs) #will give a dictionary
    for key,value in kwargs.items():
        print(kwargs["multiply"])
        
calculate(add = 3, multiply = 5) 
#add act as key and 3 acts as a value
