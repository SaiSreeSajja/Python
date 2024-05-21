func_list=[lambda x:x+2, lambda x:x*2, lambda x:x**2]
res=[func(5) for func in func_list]
print(res)

'''
[7, 10, 25]
'''