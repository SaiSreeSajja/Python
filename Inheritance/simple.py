class parent:
    def dis1(self):
        print("parent")
class Child(parent):
    def dis2(self):
        print("child")
c=Child()
c.dis2()
c.dis1()

'''
child
parents
'''