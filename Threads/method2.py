from threading import *
class Test(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread")
t=Test()
t.start()

'''
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
Child Thread
'''