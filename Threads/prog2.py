import time
def square(numbers):
    for n in numbers:
        time.sleep(2)
        print("square is:",n*n)
numbers=[2,3,4,5,6]
t=time.time()
square(numbers)
print("Done in:",time.time()-t)

'''
output:
square is: 4
square is: 9
square is: 16
square is: 25
square is: 36
Done in: 10.012248277664185
'''