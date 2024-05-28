import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)
import threading
print("Current Executing Thread:",threading.current_thread().getName())
threading.current_thread().setName("MyThread")
print("Current Executing Thread:",threading.current_thread().getName())

'''
output:
Current Executing Thread: MainThread
Current Executing Thread: MyThread
'''

'''
import threading
print("Current Executing Thread:",threading.current_thread().getName())
threading.current_thread().setName("MyThread")
print("Current Executing Thread:",threading.current_thread().getName())

output:
C:\Users\Windows 10\Desktop\ts\Threads\prog1.py:2: DeprecationWarning: getName() is deprecated, get the name attribute instead
  print("Current Executing Thread:",threading.current_thread().getName())
Current Executing Thread: MainThread
C:\Users\Windows 10\Desktop\ts\Threads\prog1.py:3: DeprecationWarning: setName() is deprecated, set the name attribute instead
  threading.current_thread().setName("MyThread")
C:\Users\Windows 10\Desktop\ts\Threads\prog1.py:4: DeprecationWarning: getName() is deprecated, get the name attribute instead
  print("Current Executing Thread:",threading.current_thread().getName())
Current Executing Thread: MyThread
'''