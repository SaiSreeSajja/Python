def sumD(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumD(n // 10)

number = int(input("Enter a number: "))
print(f"The sum of digits of {number} is {sumD(number)}.")

'''
Enter a number: 512
The sum of digits of 512 is 8.
'''