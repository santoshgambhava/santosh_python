'''
Write a Python program to count the number of characters (character frequency) in a string
'''

s="tops technologies"
print(s.count("s"))


s1=input("enter the string : ")
count=0
for i in s1:
    count=count+1
print("character frequency of string:",count)
