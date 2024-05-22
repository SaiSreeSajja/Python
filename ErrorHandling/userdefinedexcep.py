class NotEligibleException(Exception):
    def __init__(self,arg):
        self.msg=arg
age=int(input())
if age<18:
    raise NotEligibleException("You dont have vote")
else:
    print("Welcome")
    
'''
output:

10
---------------------------------------------------------------------------
NotEligibleException                      Traceback (most recent call last)
C:\PROGRA~1\KMSpico\temp/ipykernel_13148/2831520728.py in <module>
      4 age=int(input())
      5 if age<18:
----> 6     raise NotEligibleException("You dont have vote")
      7 else:
      8     print("Welcome")

NotEligibleException: You dont have vote

'''