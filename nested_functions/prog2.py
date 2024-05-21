def outer():
    print("You called outer function")
    def inner():
        return "You called inner function"
    return inner
x=outer()
x()

'''
You called outer function
You called inner function
'''