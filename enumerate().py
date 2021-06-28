'''
What is the enumerate()function in Python?
-------------------------------------------
Enumerate() method adds a counter to an iterable((list,touple,string,dict,set)) and
==> returns it in a form of {enumerate object}.
This enumerate object can then be used directly in {for loops} or be converted into
a list of tuples using {list()} method.

Syntax:
-------------
enumerate(iterable, start=0)
Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is
              to be started, by default it is 0
'''

l1 = ["eat", "sleep", "repeat","eat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))

# we can aslo apply for loop to iterate
for ele in enumerate(l1):
    print(ele,end=' ')
print()
# ------------------------------------
my_dict = {"a": 1, "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}
for i in enumerate(my_dict.values()):
  print(i)
# -----------------------------------
for i in enumerate(set(l1)) :
    print(i)