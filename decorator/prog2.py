#decorator
def decfun(func):
    def inner(a):
        if a<0:
            print("Negative val:",a)
        else:
            return func(a)
    return inner

def fun(a):
    print(a)

decorfunction=decfun(fun)


fun(-9)
decorfunction(-9)

'''
-9
Negative val: -9
'''