f=open('C:\\Users\\Windows 10\\Desktop\\ts\\textbook.txt','r')
f.seek(10,0)
data=f.read()
print(data)
f.close()

'''
output:
ere we go
These are objects
Thankyou
See you later
'''