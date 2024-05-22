import re
p=re.compile('[aeiou]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['a', 'e']
'''

import re
p=re.compile('[a-f]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['a', 'b', 'c', 'd', 'e', 'f']
'''

import re
p=re.compile('[^a-f]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

'''
['1', ' ', '1', '2', '3', ' ', ' ', '4', '5', ' ', '5', '6', ' ', '6', '7']
'''