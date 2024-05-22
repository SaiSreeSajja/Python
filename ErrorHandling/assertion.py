def sq(x):
    return x*2
assert sq(2)==4,"sq of 2 is 4"
assert sq(3)==9,"sq of 3 is 9" #these asser stmts are used to debug 
print(sq(2))

'''
output:
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
C:\PROGRA~1\KMSpico\temp/ipykernel_13148/1645588751.py in <module>
      2     return x*2
      3 assert sq(2)==4,"sq of 2 is 4"
----> 4 assert sq(3)==9,"sq of 3 is 9"
      5 print(sq(2))

AssertionError: sq of 3 is 9
'''