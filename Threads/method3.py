from threading import *
class Test:
    def display(self):
        for i in range(5):
            print("Child Thread")
t=Test()
t1=Thread(target=t.display)
t1.start()

'''
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
'''