def is_palindrome(s):
    res=''
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    if s==res:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("palindrome")
else:
    print("Not a palindrome")

'''
Enter a string: sos
palindrome
'''