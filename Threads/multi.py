import time
import threading
def square(numbers):
    for n in numbers:
        time.sleep(1)
        print("square is:",n*n)
def cube(numbers):
    for n in numbers:
        time.sleep(1)
        print("cube is:",n*n*n)
numbers=[2,3,4,5,6]
t=time.time()
t1=threading.Thread(target=square,args=(numbers,))
t2=threading.Thread(target=cube,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done in:",time.time()-t)

'''
cube is: 8
square is: 4
cube is: 27
square is: 9
cube is: 64
square is: 16
cube is: 125
square is: 25
cube is: 216
square is: 36
Done in: 5.012345552444458
'''