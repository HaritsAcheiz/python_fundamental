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

#### Copy Value
#### copy list using '=' operator
print('\norigin list')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print(mylist)
#### origin list
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
new_list = mylist
print('\ncopy list')
print(new_list)
#### copy list
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
#### But the problem when you copy in this way is when you change one of the lists,
#### either the origin list or the copy list, both of them will change.
new_list.append('item 7')
print('\norigin list')
print(mylist)
print('\ncopy list')
print(new_list)
#### origin list
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7']

#### copy list
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7']

#### to prevent that problem you can use copy method or use slicing to copy value from origin list
### Copy method
new_list = mylist.copy()
print(new_list)
### Slicing
new_list = mylist[:] # Copy all value from mylist
print(new_list)
new_list = mylist[0:3] # Copy value from mylist from index 0 until 2
print(new_list)
#### And when you change value of copied list or origin list, it will only change modified list not both.
print(mylist)
new_list = mylist[:]
print(new_list)
new_list[0] = 'modified item'
print(mylist)
print(new_list)

### Access data
print('\nindexing, access data with index number in python index number start from 0')
mylist = [1,'a',0.5,[2,'b',0.9],(3,'c',1.1),{'d':4,'e':'f','g':2.3}]
item = mylist[0]
print(item)
#### 1

print('\nindexing inside loop to access all item within list')
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

#### <list variable name> [<start index>:,<end index>:<step>]
#### start index is inclusive that means mentioned index number will be included in the selection.
#### If start parameter is not filled, default value filled by 0
#### stop index is exclusive that means mentioned index number won't be included in the selection
#### If end parameter is not filled, default value filled by last index number
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

print('\naccess data with negative end index number')
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
#### item 6
#### item 4

print('\nslicing with 2 parameter, start and end, step will use default value')
items = mylist[0:2]
for i in range(len(items)):
    print(items[i])
#### item 1
#### item 2

### Modify List
#### append method
print('\nappend 1 item')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print('\nbefore append item')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']

mylist.append('item 7')
print('\nafter append item')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7']

print('\nappend multiple items with looping')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print('\nbefore append item')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']

added_items = ['item 7','item 8']
for item in added_items:
    mylist.append(item)
print('\nafter append item')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7','item 8']

print('\nappend multiple items with extend')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print('\nbefore append item')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']

mylist.extend(added_items)
print('\nafter extend item')
print(mylist)

### Remove items

#### clear method
#### remove all item in list
print('\nbefore clear list')
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
mylist.clear()
print('\nafter clear list')
print(mylist)
#### []

#### pop method
#### remove item by index and get its value
print('\nbefore pop list')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
print('\nafter pop list')
poped_item = mylist.pop(3)
print(mylist)
print(poped_item)
#### ['item 1', 'item 2', 'item 3', 'item 5', 'item 6']
#### item 4

#### remove method
#### remove item by it's value
print('\nbefore remove list')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
print('\nafter remove list')
mylist.remove('item 2')
print(mylist)
#### ['item 1', 'item 3', 'item 4', 'item 5', 'item 6']

#### del method
#### remove items by index or slice
print('\nbefore del list')
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print(mylist)
#### ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
print('\nafter del index list')
del mylist[2]
print(mylist)
#### ['item 1', 'item 3', 'item 4', 'item 5', 'item 6']
mylist = ['item 1','item 2','item 3','item 4','item 5','item 6']
print('\nafter del slice list')
del mylist[1:3]
print(mylist)
#### ['item 1', 'item 4', 'item 5', 'item 6']



