#decorator
def decfun(func):
    def inner(a):
        if a<0:
            print("Negative val:",a)
        else:
            return func(a)
    return inner
@decfun
def fun(a):
    print(a)

fun(10)
fun(-9)

'''
10
Negative val: -9
'''