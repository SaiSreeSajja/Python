class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print(self.name,self.age)
    def dis(self,name,age):
        print(name,age)
p=Person("s",21)
#p.dis() wont work
p.dis("m",20)

'''
m 20
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self,name='',age=0):#default arguments or variable length arguments avoids error
        print(name,age)
p=Person("s",21)
p.dis()
p.dis("m",20)

'''
 0
m 20
'''
