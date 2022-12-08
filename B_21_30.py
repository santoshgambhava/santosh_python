'''
Write a Python program to create a tuple with numbers.
'''
tuplex=1,2,3,4,5,6
print(tuplex)
'''
 Write a Python program to convert a tuple to a string.
'''
t=('p','y','t','h','o','n')
str=''.join(t)
print(str)
'''
 Write a Python program to check whether an element exists within a tuple.
'''
t=('p','y','t','h','o','n')
print('p' in t)

'''
 Write a Python program to find the length of a tuple.
'''
t=('p','y','t','h','o','n')
print(len(t))

'''
 Write a Python program to convert a list to a tuple.
'''
l=[1,2,3,4,5]
tuplex=tuple(l)
print(tuplex)
'''
 Write a Python program to reverse a tuple.
'''
l=(1,2,3,4,5)
x=reversed(l)
print(tuple(x))
'''
 Write a Python program to replace last value of tuples in a list.
'''
l=[(1,2,3),(3,4,6,7)]
for i in l:
    i[:-1]+8
print(l)
'''
 a Python program to find the repeated items of a tuple.
 '''
l=(1,2,3,4,5,1,6,3,4,2,2)
count=l.count(2)
print(count)
'''
 Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
l=[(),(1,2,3),(),(3,4,6,7)]
l=[t for t in l if t]
print(l)
'''
 Write a Python program to unzip a list of tuples into individual lists.
'''
l=[(1,2,3),(3,4,6,7),(1,2),(3,4,7)]
print(list(zip(*l)))
