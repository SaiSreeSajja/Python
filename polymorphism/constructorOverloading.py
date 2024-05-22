class Person:
    def __init__(self,name):
        self.name=name
        print("Constructor called")
    def __init__(self,age):
        self.age=age
        print("Constructor called")
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Constructor called")
#p=Person("Sree") error
#p=Person(20) error
p=Person("Sree",20)

'''
Constructor called
'''

class Person:
    def __init__(self,*details):#default arguments or variable length arguments avoids error
        print("Constructor called")
p=Person("Sree") 
p=Person(20) 
p=Person("Sree",20)

'''
Constructor called
Constructor called
Constructor called
'''