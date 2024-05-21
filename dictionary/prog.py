d={}
for i in range(10):
    d[i]=chr(i+65)
print("Pairs")
for i,j in d.items():
    print((i,j),end=" ")
print("\nKeys")
for i in d.keys():
    print(i,end=" ")
print("\nValues")
for i in d.values():
    print(i,end=" ")

'''
output:
Pairs
(0, 'A') (1, 'B') (2, 'C') (3, 'D') (4, 'E') (5, 'F') (6, 'G') (7, 'H') (8, 'I') (9, 'J')
Keys
0 1 2 3 4 5 6 7 8 9
Values
A B C D E F G H I J
'''