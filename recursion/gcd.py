def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a,b=map(int,input().split())
print(f"The GCD of {a} and {b} is {gcd(a, b)}.")

'''
Enter the first number: 8
Enter the second number: 6
The GCD of 8 and 6 is 2.
'''
