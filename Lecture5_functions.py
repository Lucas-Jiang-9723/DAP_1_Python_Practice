# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:56:23 2022

@author: Lucas Jiang
"""

#%% Function Basics
#   return -- output value if we call the function
def my_func(num):
    new_num = (num * 2 + 40) / 10
    return new_num

value = my_func(10)
print(my_func(10))


#%% Function and key word arguments (kwarg)
#   Takes more than one input
def function_2(number , denominator=10):
    #denominator is 10 by default setting
    #and can be overwritten by
    new_num = (number * 2 + 40)/denominator
    return new_num
value_1 = function_2 (10)
print(value_1)
value_2 = function_2 (10, denominator = 100)
print(value_2)

#%% global value and local values
my_global = 10 #outside a function, the variable defined is global (accessible anywhere in this file)
def function_3():
    my_local = 20
    #Within a function, the variable defined is local (accessible only inside this particular function)
    return my_global * my_local
print(function_3())


#%% A practice 
names_2021 = [" jeff", "mOllY","yiJiA", "jOn", "RaHul", "noah", "bo B"]

names_2021_new = [name.strip().lower().capitalize() for name in names_2021]
print(names_2021_new)

#   Alternative Solution
def name_fix(name):
    name = name.strip().lower().capitalize().replace(" ","")
    return name
names_2021_new_2 = [name_fix(name) for name in names_2021]
print(names_2021_new_2)