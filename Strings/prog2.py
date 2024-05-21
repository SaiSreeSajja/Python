s=input().split()
for i in range(len(s)):
    if (i+1)%2==0:
        s[i]=s[i][::-1]
print(*s)

'''
one two three four five six
one owt three ruof five xis
'''