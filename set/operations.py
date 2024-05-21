s={"thus",2,4,'Mon'}
print(s)
s.add('tues')#only 1 element
print(s)
s.update([6,7])# more elements
print(s)
s.remove(2)#if not present gives error
print(s)
s.discard(2)#no error
print(s)
s.pop()
print(s)
s.clear()
print(s)
del s
#print(s) deleted so gives error

'''
output:
{2, 'thus', 4, 'Mon'}
{2, 4, 'tues', 'thus', 'Mon'}
{2, 4, 6, 7, 'tues', 'thus', 'Mon'}
{4, 6, 7, 'tues', 'thus', 'Mon'}
{4, 6, 7, 'tues', 'thus', 'Mon'}
{6, 7, 'tues', 'thus', 'Mon'}
set()
'''