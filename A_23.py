'''
Write a python function to insert a string in the middle of a string.
'''

def insert_middel(s,word):
    pos=int(len(s)/2)
    mid=s[:pos]+word+s[pos:]
    return mid
s=input("enter string:")
print(len(s))
word=input("enter your word:")
print(insert_middel(s,word))


    
