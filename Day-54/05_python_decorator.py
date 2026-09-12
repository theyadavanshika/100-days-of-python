import time
# Decorator function is just a function that wraps another function
# and gives that function some additional functionality.

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        #do something after
    return wrapper_function

#-----------------------------------------------------------#

@delay_decorator
def say_hello():
    print("hello")

@delay_decorator  #Known as syntaxtic sugar
def say_bye():
    print("bye")

def say_greeting():
    print("how are you?")

say_hello()
say_bye()

# decorated_function = delay_decorator(say_greeting)
# decorated_function() 