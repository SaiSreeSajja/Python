class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def setName(self,n):
        self.name=n
    def setAge(self,a):
        self.age=a
s=Student("Sree",20)
print(s.getAge())
s.setName("Sai Sree")
print(s.getName())

'''
20
Sai Sree
'''