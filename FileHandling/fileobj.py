with open('C:\\Users\\Windows 10\\Desktop\\ts\\textbook.txt','r') as f:
    x=f.read()
    print(x)
    print(f.closed)
print(f.closed)

'''
output:
Welcome
Here we go
These are objects
Thankyou
False
True
'''