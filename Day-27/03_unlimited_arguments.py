def add(*args):
    addition = 0
    for n in args:
        addition += n
    print(addition)
    print(type(args))
    print(args[0])

add(1,2,3,4,5,6,7,8,9,10)

#Also known as unlimited positrional agruments
# " * " operator collects all of thearguments into a tuple
