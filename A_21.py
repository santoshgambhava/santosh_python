'''
Write a Python function to reverses a string if its length is a multiple of 4.
'''
def reverse(str1):
    if len(str1)%4==0:
        return(str1[::-1])
    else:
        return(str1)
str1=input("enter string:")
print("reverses a string is:",reverse(str1))
print("str1:",str1)
