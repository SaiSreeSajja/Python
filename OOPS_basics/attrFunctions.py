class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
p1=Person(20,"Sai")
print(getattr(p1,'name'))
setattr(p1,'age',21)
print(getattr(p1,'age'))
print(hasattr(p1,'id'))
print(hasattr(p1,'age'))

'''
Sai
21
False
True
'''