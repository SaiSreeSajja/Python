class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis1(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,empid):
        super().__init__(name,age)
        self.empid=empid
    def dis(self):
        print(self.name,self.age,self.empid)
e=Employee("SS",20,'e241')
e.dis1()
e.dis()

'''
SS 20
SS 20 e241
'''