'''
map(), filter() and reduce() work in the same way: They each accept a function and a sequence of
elements and return the result of applying the received function to each element in the sequence.
'''

'''
The map() Function
----------------------
The map() function iterates through all items in
the given iterable and executes the function we passed as an argument on each of them.
'''
# syntax :
# map(function, iterable(s))

# def starts_with_A(s):
#     return s[0] == "A"     # map works on the basis epression in the function
#
# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# map_object = map(starts_with_A, fruit)    #map return itarable object
#
# print(list(map_object))
#
# # using lambda function
# map_object1 = map(lambda x : x[0]=='A',fruit)
# print(list(map_object1))

'''
The filter() Function :
-------------------------------
{filter works on th basis of True and False(means expression returns True or False),
according to that element store in new list(if element statify condition)}

Similar to map(), filter() takes a function object and an iterable and creates a new list.

As the name suggests, filter() forms a new list that contains(store) only elements that satisfy a certain
condition, i.e. the function we passed returns True.

The syntax is:

filter(function, iterable(s))
'''

# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)    #return filter object
print(filter_object)
print(list(filter_object))

# using lambda function

filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))

'''
The reduce() Function

reduce() works differently than map() and filter(). It does not return
a new list based on the function and iterable we've passed. Instead, it returns a single value.

Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:

reduce(function, sequence[, initial])
'''
# We start with a list [2, 4, 7, 3] and pass the add(x, y) function to reduce() alongside this list,
# without an initial value
#
# reduce() calls add(2, 4), and add() returns 6
#
# reduce() calls add(6, 7) (result of the previous call to add() and the next element in the list as parameters),
# and add() returns 13
#
# reduce() calls add(13, 3), and add() returns 16
#
# Since no more elements are left in the sequence, reduce() returns 16

from functools import reduce

def add(x, y):
    return x + y

list = [2, 4, 7, 3]
print(reduce(add, list))

# ----------------------------------

from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
# print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))