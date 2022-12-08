'''
Write a Python program to get the Fibonacci series of given range.
'''
n=int(input("enter number:"))
a,b=0,1
while n>b:
    print(b,end=" ")
    a,b=b,a+b
    
