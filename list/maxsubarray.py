def maxSubArray(a,l):
    maxval=float('-inf')
    for i in range(len(a)):
        sum=0
        #print(a[i:i+l])
        for j in a[i:i+l]:
            sum+=j

        if len(a[i:i+l])==4 and maxval<=sum:
            maxval=sum
            res=a[i:i+l]
    return maxval,res

l=[2,-1,4,-1,3,-5,0,22]
print(list(maxSubArray(l,4)))

'''
[20, [3, -5, 0, 22]]
'''