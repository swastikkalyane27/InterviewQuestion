'''
The difference between shallow and deep copying is only relevant for compound objects
    (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible)
{inserts references} into it to the objects found in the original.

--------------------------------------
we should go for shallow copy if all the element in the any iterable object are immutable if we did any
cheanges in original object that will not reflect in copied one and vic viz.
----------------------------------------

A deep copy constructs a new compound object and then,{ recursively,
inserts} copies into it of the objects found in the original.

------------------------------------------
if any element in object is mutable in that case we should go for deep copy ,bcz if we did any changes in
original and copied then it will not reflect in copied and original respectively
-------------------------------------------
'''
from copy import copy,deepcopy
# l1 = [1,2,3,4,5]     #all the element in l1 are immutable in such case we should go for shallow copy
# l2 = copy(l1)
# l2.append(10)
# l2.insert(2,12)
# print(l1)
# print(l2)

l3 = [1,2,[2,3,4],6,7]   # element at index 2 is mutable in such case we shold go for deepcopy
l4 = copy(l3)
l5 = deepcopy(l3)

print(id(l4[2])==id(l3[2]))        # (True) in case of copy if mutable element is there
print(id(l5[2])==id(l3[2]))        # (False) in case of deepcopy

l4[2].append(1)
l4[2].insert(1,110)
del l4[1]
l5[2].append(12)
l5[2].insert(1,15)
del l5[3]
print(l3)
print(l4)
print(l5)
