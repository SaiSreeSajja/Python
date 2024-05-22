import os
os.rename('C:\\Users\\Windows 10\\Desktop\\ts\\textbook.txt','C:\\Users\\Windows 10\\Desktop\\ts\\text.txt')
os.mkdir('C:\\Users\\Windows 10\\Desktop\\ts\\textbooks')
print(os.getcwd())
os.rmdir('C:\\Users\\Windows 10\\Desktop\\ts\\textbooks')

'''
output:
C:\Users\Windows 10\Desktop\ts\FileHandling
'''