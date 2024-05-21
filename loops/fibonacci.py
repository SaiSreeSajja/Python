n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n:
    print(a, end=' ')
    nth = a + b
    a = b
    b = nth
    count += 1

'''
Enter the number of terms: 10
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34
'''