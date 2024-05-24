from numpy import *
A=linspace(2,20,7)#start,stop,no of parts
print(A)
A=logspace(3,15,6)
print(A)
A=arange(2,20,3)#start,stop,step
print(A)
A=zeros(6,int)
print(A)
A=ones(6,int)
print(A)
print(A.dtype)
print(A.ndim)
print(A.size)
print(A.shape)

'''
output:
[ 2.  5.  8. 11. 14. 17. 20.]
[1.00000000e+03 2.51188643e+05 6.30957344e+07 1.58489319e+10
 3.98107171e+12 1.00000000e+15]
[ 2  5  8 11 14 17]
[0 0 0 0 0 0]
[1 1 1 1 1 1]
int32
1
6
(6,)
'''