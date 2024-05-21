def sumD(res):
    sum=0
    while(res>0):
        b=res%10
        sum+=b
        res=res//10
    return sum

print(sumD(int(input("Enter a number:"))))

'''
Enter a number:512
8
'''
