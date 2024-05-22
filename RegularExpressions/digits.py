import re
p=re.compile('\d+')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['1', '123', '45', '56', '67']
'''

p=re.compile('\D')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['a', 'b', 'c', ' ', ' ', 'd', 'e', 'f', ' ', ' ', ' ']
'''

p=re.compile('[0-8][0-8]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['12', '45', '56', '67']
'''