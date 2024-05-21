s=input()
e=''
o=''
for i in range(len(s)):
    if (i+1)%2==0:
        e+=s[i]
    else:
        o+=s[i]
print(e)
print(o)

'''
goodmorning
odonn
gomrig
'''