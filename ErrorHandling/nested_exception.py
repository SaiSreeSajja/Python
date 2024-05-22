try:
    print(10/int(input()))
except ZeroDivisionError:
    print("Dont give zero as input")
    try:
       print(10/int(input())) 
    except ValueError:
        print("Give only integer")
    finally:
        print("Inner block")
finally:
    print("Done")
    
'''
output:
0
Dont give zero as input
ten
Give only integer
Inner block
Done
'''