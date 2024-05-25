from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def display(self):
        print("You are accessing the shape class")

class Rectangle(Shape):
    a=10
    b=5
    def area(self):
        print(self.a*self.b)
    def perimeter(self):
        print(2*(self.a+self.b))

r=Rectangle()
r.area()
r.perimeter()
r.display()

class Square(Shape):
    s=5
    def area(self):
        print(self.s*self.s)
    def perimeter(self):
        print(4*(self.s))
    def display(self):
        print("square class")

sq=Square()
sq.area()
sq.perimeter()
sq.display()

'''
output:
50
30
You are accessing the shape class
25
20
square class
'''


    

        

