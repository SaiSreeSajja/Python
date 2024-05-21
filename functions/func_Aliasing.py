def greets():
    print("Welcome")
wish=greets
greets()
wish()
#function aliasing
print(id(wish),id(greets))

'''
Welcome
Welcome
2129102078160 2129102078160
'''