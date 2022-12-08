'''
Write a Python program to get the Factorial number of given number.
'''
n=int(input("enter number"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print("factorial:",fact)
    
