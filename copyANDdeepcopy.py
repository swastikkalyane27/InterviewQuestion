'''
The difference between shallow and deep copying is only relevant for compound objects
    (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible)
inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively,
inserts copies into it of the objects found in the original.
'''