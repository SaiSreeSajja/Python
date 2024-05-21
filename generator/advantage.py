g=(x*x for x in range(10000000000000))
print(next(g))

#output:0

#l=[x*x for x in range(10000000000000)] it raises MemoryError
#print(l[0])