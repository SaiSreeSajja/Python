from datetime import *
x=datetime.now()
print(x)
print(x.date())
print(x.time())
print(x.strftime('%A')) 
print(x.strftime('%a'))
print(x.strftime('%B')) 
print(x.strftime('%b')) 
print(x.strftime('%Y')) 
print(x.strftime('%y')) 
 
 
'''
output:
2024-05-24 12:31:07.332293
2024-05-24
12:31:07.332293
Friday
Fri
May
May
2024
24 
'''