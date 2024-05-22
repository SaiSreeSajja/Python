
class grandpa:
    def dis1(self):
        print("Grandpa")
class parent(grandpa):
    def dis2(self):
        print("parent")
class Child(parent):
    def dis3(self):
        print("child")
c=Child()
c.dis1()
c.dis2()
c.dis3()

'''
Grandpa
parent
child
'''