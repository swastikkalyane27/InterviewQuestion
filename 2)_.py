'''
What is the iterator protocol?
--------------------------------------
Iterator in Python is simply an object that can be iterated upon. An object
which will return data, one element at a time. Technically speaking,
a Python iterator object must implement two special
methods, __iter__() and __next__() , collectively called the iterator protocol.
---------------------------------------
An object is called iterable if we can get an iterator from it.
 Most built-in containers in Python like: list, tuple, string etc. are iterables.
The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
---------------------------------------
We use the next() function to manually iterate through all the items of an iterator. When we reach
 the end and there is no more data to be returned, it will raise the StopIteration Exception
'''

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter() (create iterator form by using iter() fun then only we can iterate on in manually by
# using next()

my_iter = iter(my_list)       #(also we can create itreater object by my_list.__iter__())

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)

