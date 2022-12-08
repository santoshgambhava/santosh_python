'''
Write a Python program to add 'ing' at the end of a given string (length shouldbe at least 3).
If the given string already ends with 'ing' then add 'ly' instead if the string length of the
given string is less than 3, leave it unchanged.
'''
s=input("enter string:")
if len(s)>=3:
    if s[-3:]=="ing":
        s=s+"ly"
        print(s)
    else:
        s=s+"ing"
        print(s)
else:
    print(s)
    
