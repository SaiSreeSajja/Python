def ll(a):
    l=[]
    for i in a:
        for j in i:
            l.append(j)
    return l

print(ll([[1,2,33,4],[21,7,3],[6,7,8]]))

def ll2(a):
    l=[]
    for i in a:
        l.extend(i)
    return l

print(ll2([[1,2,33,4],[21,7,3],[6,7,8]]))

'''
[1, 2, 33, 4, 21, 7, 3, 6, 7, 8]
[1, 2, 33, 4, 21, 7, 3, 6, 7, 8]
'''