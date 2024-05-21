def count(n):
    for i in range(n,-1,-1):
        yield i

vals=count(5)
for j in vals:
    print(j)

'''
5
4
3
2
1
0
'''