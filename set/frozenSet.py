f=frozenset((1,2,3,4,5,2,3))
print(type(f))
for i in f:
    print(i,end=" ")
#f.discard(2)
#f.add(9) These wont work as frozenset is immutable
'''
output:
<class 'frozenset'>
1 2 3 4 5
'''