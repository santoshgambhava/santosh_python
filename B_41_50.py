'''
 Write a Python program to map two lists into a dictionary
'''
def test(keys,values):
    return dict(zip(keys,values))
l1=['a','b','c','d','e']
l2=[1,2,3,4,5]
print(test(l1,l2))
'''
 Write a Python program to combine two dictionary adding values for common keys.
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}
for key in d1:
    if key in d2:
        d2[key]=d1[key]+d2[key]
    else:
        d2[key]=d1[key]
print(d2)



'''
 Write a Python program to print all unique values in a dictionary
'''
'''
 Write a Python program to create and display all combinations of letters, selecting each
 letter from a different key in a dictionary.
o Sample data: {'1': ['a','b'], '2': ['c','d']}
o Expected Output:
o ac ad bc bd
'''
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
'''
 Write a Python program to find the highest 3 values in a dictionary
'''
'''
 Write a Python program to combine values in python list of dictionaries. Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
o {'item': 'item1', 'amount': 750}]
o Expected Output: Counter ({'item1': 1150, 'item2': 300})
'''
'''
 Write a Python program to create a dictionary from a string.
o Note: Track the count of the letters from the string. Sample string: 'w3resource'
o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
'''
'''
 Write a Python function to calculate the factorial of a number (a non-negative integer)
'''
