# def calculate(n, **kwargs): 
#     print(kwargs) 
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
        
# calculate(9, add = 3, multiply = 5)
#add act as key and 3 acts as a value


# class car:

#     def __init__(self, **kwarg):
#         self.make = kwarg["make"]
#         self.model = kwarg["model"]

# my_car = car(make = "new", model = "GT-R")
# print(my_car.make)


class car:

    def __init__(self, **kwarg):
        self.make = kwarg["make"]
        self.model = kwarg.get("model") #same as sq bracket but the benifit is that if that key does'nt in the dict then i'll just return none.wont give error

my_car = car(model = "GT-R")
print(my_car.model)



