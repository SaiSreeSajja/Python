class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def hlo(self,z):
        self.z=z
m=Test(10,5)
print(m.__dict__)
m.hlo(2)
print(m.__dict__)
m.d=40
print(m.__dict__)
'''
{'x': 10, 'y': 5}
{'x': 10, 'y': 5, 'z': 2}
{'x': 10, 'y': 5, 'z': 2, 'd': 40}
'''