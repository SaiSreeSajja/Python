l=[x**2 for x in range(1,10)]
print(l)

m=[i for i in range(10) if i%2==0]
print(m)

n=["even" if i%2==0 else "odd" for i in range(10)]
print(n)

a=[1,2,3,4]
b=[4,3,2,1]
o=[[i,j] for i in a for j in b]
print(o)

x=[[int(input()) for j in range(3)] for i in range(3)]
print(x)#3x3 matrix


'''
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8]
['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
[[1, 4], [1, 3], [1, 2], [1, 1], [2, 4], [2, 3], [2, 2], [2, 1], [3, 4], [3, 3], [3, 2], [3, 1], [4, 4], [4, 3], [4, 2], [4, 1]]
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''