l={x:x**2 for x in range(1,10)}
print(l)

n={i:"even" if i%2==0 else "odd" for i in range(10)}
print(n)

a={1,2,3,4}
b={4,3,2,1}
o={i:(i,j) for i in a for j in b}
print(o)

x={i:[int(input()) for j in range(3)] for i in range(3)}
print(x)#3x3 matrix

'''
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd'}
{1: (1, 4), 2: (2, 4), 3: (3, 4), 4: (4, 4)}
2
3
5
1
7
8
4
5
9
{0: [2, 3, 5], 1: [1, 7, 8], 2: [4, 5, 9]}
'''