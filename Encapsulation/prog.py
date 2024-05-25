class Test:
    x=10 #public
    _y=8 #protected
    __z=2 #private
    def __init__(self):
        print("Inside the class")
        print(self.x)
        print(self._y)
        print(self.__z)

t=Test()
print("outside the calss")
print(t.x)
print(t._y)
#print(t.__z) private variable is accessed only inside the class

class Test2(Test):
    def __init__(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

t2=Test2()

'''
Inside the class
10
8
2
outside the calss
10
8
10
8
Traceback (most recent call last):
  File "C:\Users\Windows 10\Desktop\ts\Encapsulation\prog.py", line 23, in <module>       
    t2=Test2()
       ^^^^^^^
  File "C:\Users\Windows 10\Desktop\ts\Encapsulation\prog.py", line 21, in __init__       
    print(Test.__z)
          ^^^^^^^^
AttributeError: type object 'Test' has no attribute '_Test2__z'. Did you mean: '_Test__z'?
'''