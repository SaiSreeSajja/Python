s=input()
d={}
for i in s:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i,j in d.items():
    print("{}-{}".format(i,j),end=',')

'''
hhumjkoapaaajkose
h-2,u-1,m-1,j-2,k-2,o-2,a-4,p-1,s-1,e-1,
'''