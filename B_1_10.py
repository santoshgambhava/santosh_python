'''
1. What is List? How will you reverse a list?
'''
#list is group of data
l=[1,2,4,"tpos","True",20,1.1]
print(l[::-1])


'''
 How will you remove last object from a list?
'''
l=[1,2,4,"tpos","True",20,1.1]
l.pop()
print(l)


'''
 Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?
'''
l=[2, 33, 222, 14,25]
print(l[-1])


'''
 Differentiate between append () and extend () methods?
'''
l=[2, 33, 222, 14,25]
l.append(10)
print(l)
l.extend([30,40,50])
print(l)

'''
 Write a Python function to get the largest number, smallest num and sum of all from a list.
'''
'''
 How will you compare two lists?
'''
l1=[1,2,3,4]
l2=[1,2,3,5,4]
l1.sort()
l2.sort()
if l1==l2:
    print("the list are identical")
else:
    print("the list are not identical")

'''
 Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.
'''
l=["tops","xyx","Technologies","121","aa"]
s=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        print("the given strings are:",i)
        s=s+1
print ("no. of string you want:",s)

'''
 Write a Python program to remove duplicates from a list.
'''
l=[1,2,5,3,1,6,7,4,8,9,5]
dup_items=[]
for i in l:
    if i not in dup_items:
        dup_items.append(i)
print(dup_items)


'''
 Write a Python program to check a list is empty or not.
'''
l=[1,2,3]
if l==[]:
    print("liist is empty")
else:
    print("liist is not empty")

'''
 Write a Python function that takes two lists and returns true if they have at least one
common member.
'''
l1=[1,3,5,7,8]
l2=[3,5,6,7,9]

def comman_data(l1,l2):
    for x in l1:
        for y in l2:
            if x==y:
                
                return True
print(comman_data([1,2,3,4],[4,5,1,9]))
