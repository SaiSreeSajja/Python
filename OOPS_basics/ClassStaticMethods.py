class Tell:
    a=10
    def __init__(self):
        print(self.a)
        print(Tell.a)
    @classmethod
    def m1(cls):
        print(cls.a)
        Tell.a=100
        print(Tell.a)
    @staticmethod
    def m2():
        Tell.a+=10
        print(Tell.a)
        
t=Tell()
t.m1()
t.m2()

'''
10
10
10
100
110
'''