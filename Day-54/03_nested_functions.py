#Nested Functions

def outer_function():
    print("I'm an outer function")

    def nested_function():
        print("I'm an inner function") 

    nested_function()

outer_function()


