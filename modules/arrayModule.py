from array import *
A=array('i',[1,2,3,4])
B=array('f',[1.3,2.4])

print(B)
print(A)
print(type(A))
print(A.typecode)
print(A[2])
A.insert(1,34)
print(A)
A.append(45)
print(A)
A.extend([67,89,90])
print(A)
A.remove(34)
print(A)
A.reverse()
print(A)

'''
output:
array('f', [1.2999999523162842, 2.4000000953674316])
array('i', [1, 2, 3, 4])
<class 'array.array'>
i
3
array('i', [1, 34, 2, 3, 4])
array('i', [1, 34, 2, 3, 4, 45])
array('i', [1, 34, 2, 3, 4, 45, 67, 89, 90])
array('i', [1, 2, 3, 4, 45, 67, 89, 90])
array('i', [90, 89, 67, 45, 4, 3, 2, 1])
'''