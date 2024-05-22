import re
p=re.compile('\s')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)
#[' ', ' ', ' ', ' ', ' ']

import re
p=re.compile('\S')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)
#['a', 'b', 'c', '1', '1', '2', '3', 'd', 'e', 'f', '4', '5', '5', '6', '6', '7']