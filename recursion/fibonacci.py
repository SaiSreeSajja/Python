def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter no. of terms: "))
print(f"The {n}-th term in the Fibonacci sequence is {fibonacci(n)}.")

'''
Enter no. of terms: 10
The 10-th term in the Fibonacci sequence is 34.
'''
