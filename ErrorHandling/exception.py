try:
    print(10/int(input()))
except ZeroDivisionError:
    print("Dont give zero as input")
except ValueError:
    print("Give integer")
finally:
    print("Done")
    
'''
output:
0
Dont give zero as input
Done
'''