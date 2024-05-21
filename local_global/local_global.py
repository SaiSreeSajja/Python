a=11
def fun():
    a=90
    print(a)
    print(globals()['a'])
fun()
'''
90
11
'''