'''
Write a Python program to convert a list of tuples into a dictionary.
'''
l=[("A",1),("B",2),("C",3)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)


'''
How will you create a dictionary using tuples in python?
'''
l=[("A",1),("B",2),("C",3)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)


'''
Write a Python script to sort (ascending and descending) a dictionary by value.
'''
import operator
d={1:2,2:3,3:4,4:5,5:6}
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1)))
print("dictionary in accending order by value:",sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print("dictionary in descending order by value:",sorted_d)

'''
Write a Python script to concatenate following dictionaries to create a new one.
'''
 
'''
Write a Python script to check if a given key already exists in a dictionary.
'''
d={1:2,2:3,3:4,4:5,5:6}
def is_key_present(x):
    if x in d:
        print("key is already present in dictionary")
    else:
        print("key is not present in dictionary")
is_key_present(5)
is_key_present(8)

'''
How Do You Traverse Through A Dictionary Object In Python?
'''
'''
How Do You Check The Presence Of A Key In A Dictionary?
'''
'''
Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
'''
d=dict()
for x in range(1,15):
    d[x]=[x**2]
print(d)
'''
Write a Python program to check multiple keys exists in a dictionary
'''

'''
Write a Python script to merge two Python dictionaries
'''
d1={1:"santosh",2:"khushali",3:"dhruvi"}
d2={4:"janvi",5:"dhruv",6:"dhara"}
d3={**d1,**d2}
print(d3)
