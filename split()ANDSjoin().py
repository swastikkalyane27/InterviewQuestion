'''
Explain join() and split() in Python.

You can use split() function to split a string based on a delimiter to a list of strings.
You can use join() function to join a list of strings based on a delimiter to give a single string.
--------------------------
'''
# 1) split() function
# --------------------------
# split() method returns a list of strings after breaking the given string by the specified separator.
# If it is not provided, then any white space is a separat

# syntax:
# --------------------------
# str.split(separator,max-split)
# separator – This is is a delimiter. The string splits at the specified separator.
# max-split – This provides the maximum no of splits to make. If no value is provided, there is no limit.
# ----------------------------
str = 'hello guys how are you'
str1 = 'hello-how-are-you-am-fine'
x = str.split()
y = str1.split('-',3)
print(x)   # return list of element
print(y)

# ----------------------------
# 2. Join() – It joins each element of an iterable (such as list, string and tuple)
# by a string separator (the string on which the join() method is called) and returns the concatenated string.
# Syntax : 'string_separator'.join(iterable)
list1 =['a','b','c','d']
dict1 = {'a':1,'b':1}
list3 =set(list1)
list2 = tuple(list1)
# Example 1-
a = "".join(list1)
b = "".join(list2)
c = "".join(list3)
d = "".join(dict1.keys())
print(a)
print(b)
print(c)
print(d)
# Output: ABCD