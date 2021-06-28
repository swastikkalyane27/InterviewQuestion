'''
What do you mean by *args and **kwargs?
---------------------------------------------
we define a function to make a reusable code that performs similar operation.
To perform that operation, we call a function with the specific value,
this value is called a function argument in Python.

'''
def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)
# adder(10,12,13,14)     # if we passed more or less than defined argument it gives error

# to overcome such cases we should use *args for non keyword argument and **kwargs for key word argument and we don't know
# how much args is there
#  *args --> in touple
# **kwargs --> in dict
# ----------------------
# for *args
# -----------------
def adder(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:", sum)

# we can to this by another way by passing list of args but *args is the ifficent way to do

# sum_integers_list.py
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
# ----------------
# for **args
# -------------
adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# -----------------------------------------------------------
# the order or * & ** args
#==> *args ---> **args     in other case it will raise error
# -----------------------------------------------------------

# unpacking by using * and **
# -------------------------------
# print_list.py
my_list = [1, 2, 3]
print(my_list)

my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

