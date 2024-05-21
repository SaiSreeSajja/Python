#Reversing
s=input()
res=''
for i in range(len(s)-1,-1,-1):
    res+=s[i]
print(res)

'''
saisree
eersias
'''

s=input()
print("".join(reversed(s)))

'''
welcome
emoclew
'''

s=input().split()
print(" ".join(reversed(s)))

'''
hi my name is sai sree
sree sai is name my hi
'''