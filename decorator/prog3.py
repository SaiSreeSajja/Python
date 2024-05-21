def readying(func):
    def inner():
        print("hair styling")
        print("makeup")
        func()
    return inner
@readying
def getReady():
    print("Ready")
    
getReady()

"""
hair styling
makeup
Ready
"""