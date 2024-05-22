import re
e='ababbaabbb'
p=re.compile('ab*')
ans=p.findall(e)
print(ans)
#['ab', 'abb', 'a', 'abbb']

p=re.compile('ab?')
ans=p.findall(e)
print(ans)
#['ab', 'ab', 'a', 'ab']

p=re.compile('ab+')
ans=p.findall(e)
print(ans)
#['ab', 'abb', 'abbb']
