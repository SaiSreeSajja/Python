class parent:
    def dis(self):
        print("parent")
class Child(parent):
    def dis(self):
        print("child")
c=Child()
c.dis()

p=parent()
p.dis()

'''
child
parent
'''