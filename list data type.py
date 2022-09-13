"""
This Program gives us knowledge about list data type
"""

# List
## Definition
#### List is Muteable Sequence data type that could store homogeneous (single data type) or heterogeneous (multiple data type) items.
#### It can be filled by primitive data type, non-primitive or both.
#### It's written as a list of comma-separated element enclosed within square brackets.

## Syntax
### Assign Value

print('\nassign empty list')
mylist = []
print(mylist)
print(type(mylist))
#### []
#### <class 'list'>

print('\nassign heterogeneous data type items')
mylist = [1,'a',0.5,[2,'b',0.9],(3,'c',1.1),{'d':4,'e':'f','g':2.3}]
print(mylist)
print(type(mylist))
#### [1, 'a', 0.5, [2, 'b', 0.9], (3, 'c', 1.1), {'d': 4, 'e': 'f', 'g': 2.3}]
#### <class 'list'>

### Access data
print('\nindexing, access data with index number in python index number start from 0')
mylist = [1,'a',0.5,[2,'b',0.9],(3,'c',1.1),{'d':4,'e':'f','g':2.3}]
item = mylist[0]
print(item)
#### 1

print('\nindexing inside loop to access all item with index')
for i in range(len(mylist)):
    print(mylist[i])
#### 1
#### a
#### 0.5
#### [2, 'b', 0.9]
#### (3, 'c', 1.1)
#### {'d': 4, 'e': 'f', 'g': 2.3}

print('\naccess selected items with slicing')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
items = mylist[::]
for i in range(len(items)):
    print(items[i])

#### <list variable name> [<start index>:,<stop index>:<step>]
#### start index is inclusive that means mentioned index number will be included in the selection.
#### If start parameter is not filled, default value filled by 0
#### stop index is exclusive that means mentioned index number won't be included in the selection
#### If stop parameter is not filled, default value filled by last index number
#### If step parameter is not filled, default value filled by 1

print('\naccess data with index number between 2 and 4 (excluesive) with 1 step sequence')
items = mylist[2:4:1]
for i in range(len(items)):
    print(items[i])
#### item 3
#### item 4

print('\naccess data with index number between 2 and 5 (excluesive) with 2 step sequence')
items = mylist[2:5:2]
for i in range(len(items)):
    print(items[i])
#### item 3
#### item 5

print('\naccess data with negative start index number')
items = mylist[-3::]
for i in range(len(items)):
    print(items[i])
#### item 4
#### item 5
#### item 6

print('\naccess data with negative stop index number')
items = mylist[:-3:]
for i in range(len(items)):
    print(items[i])
#### item 1
#### item 2
#### item 3

print('\naccess data with negative step index number')
items = mylist[::-2]
for i in range(len(items)):
    print(items[i])
#### item 6
#### item 4
#### item 2

print('\naccess data with negative parameter index number')
items = mylist[-1:-4:-2]
for i in range(len(items)):
    print(items[i])