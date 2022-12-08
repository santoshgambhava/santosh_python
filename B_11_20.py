'''
Write a Python program to generate and print a list of first and last 5 elements where the
values are square of numbers between 1 and 30.
'''
def printvalues():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
printvalues()


'''
 Write a Python function that takes a list and returns a new list with unique elements of the
first list.
'''
def unique_list(l):
    unique=[]
    for i in l:
        if i not in unique:
            unique.append(i)
    return unique
print(unique_list([1,2,3,5,2,6,4,3,8,5]))
    
    
'''
 Write a Python program to convert a list of characters into a string.
'''
l=['p','y','t','h','o','n']
str1=''.join(l)
print(str1)
'''
 Write a Python program to select an item randomly from a list.
'''
import random
l=['p','y','t','h','o','n']
random= random.choice(l)
print("random:",random)

'''
 Write a Python program to find the second smallest number in a list.
'''

            
'''
 Write a Python program to get unique values from a list
'''
l=[1,3,4,6,2,7,4,6,9,3]
list1=set(l)
list2=list(list1)
print("list of unique number:",list2)

'''
 Write a Python program to check whether a list contains a sub list
'''
l=[[1,3,4],[6,2,7],[4,6,9,3]]
l1=[1,3,4]
if l1 in l:
    print("list is present")
else:
    print("list is not present")
'''
 Write a Python program to split a list into different variables.
'''
l=['p','y','t','h','o','n']
for i in l:
    print(i)
l1,l2,l3,l4,l5,l6=l
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
'''
 Write a Python program to create a tuple with different data types.
'''
tuplex=("tuple",False,3.2,1)
print(tuplex)
