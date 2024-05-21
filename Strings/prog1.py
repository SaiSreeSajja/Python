s=input()
for i in range(len(s)):
    if s[i].isnumeric():
        print(chr(ord(s[i-1])+int(s[i])),end='')
    else:
        print(s[i],end='')

'''
a4k3b2
aeknbd
'''