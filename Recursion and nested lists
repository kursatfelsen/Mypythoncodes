"""Write a recursive function named "branch" that takes as arguments a list of indices and a nested list structure. It should return the item indexed by the first argument. It works like "[]" operator is applied multiple times to the second list.

Sample Run:

>>> branch([2], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]) 
['e', 'f']
>>> branch([2, 1], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]) 
'f' 
>>> branch([1, 2, 0, 1], [['a', 'b'], [['c', 'd'], ['e', 'f'], [['g', 'h'], ['i', 'j']], 'k'], ['l', 'm']])
'h'
"""
def branch(count,items):
    if len(count)==1:
        return items[count[0]]
    return branch(count[1:],items[count[0]])

-----------------------------------
"""
2. Flatten

Write a function named "flatten" that flattens a nested list.

Sample Run:

>>> flatten([1,2,3,4])
[1, 2, 3, 4]
>>> flatten([1,[2],3,4])
[1, 2, 3, 4]
>>> flatten([1,[[2],3],4])
[1, 2, 3, 4]
>>> flatten([1,[[2],3],[[[4]]]])
[1, 2, 3, 4]

"""


def helper(item):
    if len(item)==1:
        if type(item[0])==int:
            return [item[0]]
        else:
            return helper(item[0])
    else:
        if item[0]==int:
            return item[0]+helper[1:]
        else:
            return helper(item[0])
def flatten(items):
    if type(items[0])==int:
        return flatten(items[1:])
    else:
      	items[0]=help(items[0])
        return items[0]+flatten(items[1:])
        
#!!! DIDNT WORK
