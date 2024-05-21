def outer():
    print("in outer")
    def inner():
        print("in inner")
    inner()
outer()
#inner() funtion can not be called outside of outer function


'''
in outer
in inner
'''