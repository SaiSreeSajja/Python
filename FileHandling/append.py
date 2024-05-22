f=open('C:\\Users\\Windows 10\\Desktop\\ts\\textbook.txt','a')
f.write("\nSee you later")
f=open('C:\\Users\\Windows 10\\Desktop\\ts\\textbook.txt','r')
data=f.read()
print(data)
f.close()

'''
output:
Welcome
Here we go
These are objects
Thankyou
See you later
'''