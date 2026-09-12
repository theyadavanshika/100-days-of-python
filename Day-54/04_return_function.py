#Functions can be returned from other function

def outer_function():
    print("I'm an outer function")

    def nested_function():
        print("I'm an inner function") 

    return nested_function 

inner_function = outer_function() 
inner_function()  