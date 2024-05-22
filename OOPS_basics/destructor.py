class Test:
    def __init__(self):
        print("obj created")
    def __del__(self):
        print("obj deleted")
t=Test()
t=None
t1=Test()
del t1

'''
obj created
obj deleted
obj created
obj deleted
'''