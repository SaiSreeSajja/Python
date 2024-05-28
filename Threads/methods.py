import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
from threading import *
import time
def f1():
    print(current_thread().getName(),"...started",current_thread().ident)
    time.sleep(3)
    print(current_thread().getName(),"...ended",current_thread().ident)
print("The no of active threads:",active_count())
t1=Thread(target=f1,name="thread1")
t2=Thread(target=f1,name="thread2")
t3=Thread(target=f1,name="thread3")
t1.start()
t2.start()
t3.start()
print("The no of active threads:",active_count())
print(t2.name,"is Alive:",t2.is_alive())
time.sleep(5)
print(t1.name,"is Alive:",t1.is_alive())
t1.join(5)
for i in range(5):
    print("mainthread")

'''
output:
The no of active threads: 1
thread1 ...started 21620
thread2 ...started 9068
thread3 ...started 19756
The no of active threads: 4
thread2 is Alive: True
thread3 ...ended 19756
thread1 ...ended 21620
thread2 ...ended 9068 
thread1 is Alive: False
mainthread
mainthread
mainthread
mainthread
mainthread
'''