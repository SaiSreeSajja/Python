h='hlo'
def greet():
    print(h)
def greetings():
    global h
    h="hello"
    print(h)
def greets():
    print(h)
greet()
greetings()
greets()

'''
output:
hlo
hello
hello
'''