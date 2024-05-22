
class Person:
    def dis1(self):
        print("Person")
class Adult(Person):
    def dis2(self):
        print("Adult")
class Child(Person):
    def dis3(self):
        print("child")
print("Child class:")
c=Child()
c.dis1()
c.dis3()
print("Adult class:")
a=Adult()
a.dis1()
a.dis2()
'''
Child class:
Person
child
Adult class:
Person
Adult
'''