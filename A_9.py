'''
Write a Python program to sum of three given integers. However, if two
values are equal sum will be zero.
'''
def sumofthree(a,b,c):
    if a==b or b==c or c==a:
        sum=0
    else:
        sum=a+b+c
    return sum
print(sumofthree(1,2,3))


        
