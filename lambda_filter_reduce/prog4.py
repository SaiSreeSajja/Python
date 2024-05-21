operations={
    'add':lambda x,y:x+y,
    'sub':lambda x,y:x-y,
    'mul':lambda x,y:x*y,
}

res_add=operations['add'](5,3)
res_sub=operations['sub'](4,3)
res_mul=operations['mul'](8,3)

print(res_add,res_sub,res_mul)

'''
8 1 24
'''