# ## default args
# def add(a,b=5,c=10):
#     return (a+b+c)

# # print(add(3))
# # print(add(3,4))
# print(add(2,3,4))


# ## keyword args
# def add(a,b=5,c=10):
#     return (a+b+c)

# print (add(b=10,c=15,a=20))
# print (add(a=20))


# ## positional args
# def add(a,b=5,c=10):
#     return (a+b+c)

# print (add(10,20,30))
# print (add(10,c=30,b=20))


# #1. default arguments should follow non-default arguments
# def add(a=5,b,c):
#     return (a+b+c)


# #2. keyword arguments should follow positional arguments
# def add(a,b,c):
#     return (a+b+c)

# print (add(a=10,3,4))

# #3. All the keyword arguments passed must match one of the arguments accepted by the function and their order 
# # is not important.
# def add(a,b,c):
#     return (a+b+c)

# print (add(a=10,b1=5,c=12))

# #4. No argument should receive a value more than once
# def add(a,b,c):
#     return (a+b+c)

# print (add(a=10,b=5,b=10,c=12))

# #5. Default arguments are optional arguments
# # Example 1: Giving only the mandatory arguments
# def add(a,b=5,c=10):
#     return (a+b+c)

# print (add(2))

# # Example 2: Giving all arguments(optional and mandatory arguments)
# def add(a,b=5,c=10):
#     return (a+b+c)

# print (add(2,3,4))

#--------------------------------------------------------------------------------------------------------------

## variable length args
# arbitrary positional args
# def add(*b):
#     result=0
#     for i in b:
#          result=result+i
#     return result

# print (add(1,2,3,4,5))
# print (add(10,20))

# arbitrary keyword args
# def fn(**a):
#     for i in a.items():
#         print (i)
# fn(numbers=5,colors="blue",fruits="apple")


#1. positional or keyword args
# def add(a,b,c):
#     return a+b+c

# print (add(3,4,5))
# print (add(3,c=1,b=2))


#2. positional only parameters
# def add(a,b,/,c,d):
#     return a+b+c+d

# print (add(3,4,5,6))
# print (add(3,4,c=1,d=2))

# if we specify the keyword arg for positional only args 
# def add(a,b,/,c,d):
#     return a+b+c+d

# print (add(3,4,1,d=2))


#3. keyword only argument
# def add(a,b,*,c,d):   # (position only / position or kw * kw)
#     return a+b+c+d

# print (add(3,4,c=1,d=2))


# if we specify the position arg for keyword only args 
# def add(a,b,*,c,d):
#     return a+b+c+d

# print (add(3,4,1,d=2))

#------------------------------------------------------------------------------------------------

# all 3 calling conventions used in same function
# def add(a,b,/,c,*,d):
#     return a+b+c+d

# print (add(3,4,1,d=2))
