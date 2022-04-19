# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:12:03 2022

@author: Lucas Jiang
"""

#%% function as arguments
#   Global value should be all cap letters
BASE_VAL = 100

def value_tester (a,b):
    val = sum([a,b])
    if val > BASE_VAL:
        statement = "bigger than"
    elif val == BASE_VAL:
        statement = "the same as"
    else:
        statement = "smaller than"
        
    print(f"First number:{a}; Second number:{b}; The value is {statement} the base value.")

import random
a = random.randint(25,75)
b = random.randint(25,75)
value_tester(a,b)

x = value_tester(a,b)
#%% Unpacking notation review

x , y = [10, 20]
print(x)
print(y)

# the star notation takes whatever is left and inputs in the object
x, *y = [10, 20, 30]
print(x)
print(y)

#%% using the star notation upacking to deal with unmatched argument number in function input
#   sum takes a list as argument

def value_tester(*ab):
    val = sum(ab)
    if val > BASE_VAL:
        statement = "bigger than"
    elif val == BASE_VAL:
        statement = "the same as"
    else:
        statement = "smaller than"
        
    print(f"The value is {statement} the base value.")

value_tester(50,50)


#%% Functions themselves are objects

sum_function = sum
#   this is copying the content of the sum function and pass it to the new funciton
print(sum_function([50,50]))


#%% Function as arguments
def value_tester(*ab,key_function=sum):
    val = key_function(ab)
    if val > BASE_VAL:
        statement = "bigger than"
    elif val == BASE_VAL:
        statement = "the same as"
    else:
        statement = "smaller than"
        
    print(f"The value is {statement} the base value.")

value_tester(50,50)
import numpy as np
value_tester(10, 10, key_function=np.prod)


#%% Anonymous functions aka lambda functions
def avg(a, b):
    return (a + b) / 2

lambda a, b: (a + b) /2
#lambda function is anonymous does not have a name

value_tester(10, 10, key_function=lambda ab: sum(ab)/len(ab))

# we can of course assign lambda functions to a name, but it makes no sense



#%% Class inheritance

class Vehicle():
    def __init__(self, kind):
        self.kind = kind
        
    def what_am_i(self):
        print(f"I am a {self.kind}.")
    
    def fuel(self):
        print("I use oil for fuel.")

vehicle = Vehicle("car")
vehicle.what_am_i()
vehicle.fuel()


# inheritence: take an existing class and use it as a foundation of another class
class Bicycle(Vehicle):
    def fuel(self):
        print("I am people-powered.")
    
    def peddle_me(self):
        print("You have to peddle fast.")

# in this e.g. everything from the Vehicle class is inherited in the Bicycle class, while the fuel method is over-written

bike = Bicycle("bike")
bike.what_am_i()
bike.fuel()
bike.peddle_me()

#   another e.g.
class new_str(str):
    def say_hello(self):
        print("hello world")
    
    def lower(self):
        print("NO! I DON'T WANT TO BE IN LOWER CASE!")
    #overwriting lower()
    
ms = new_str("Hi! This is Lucas")
ms.lower()
ms.upper()
ms.say_hello()