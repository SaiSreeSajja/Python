class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=self.Age(age)
    def display(self):
        print(self.name)
    class Age:
        def __init__(self,yr):
            self.yr=2024-yr
        def display(self):
            print(self.yr)
p=Person("Sree",20)
p.display()
x=p.age
x.display()

'''
Sree
2004
'''