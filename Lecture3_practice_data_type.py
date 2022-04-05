# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:27:21 2022

@author: Lucas Jiang
"""

#%%
import datetime



#%% 
# basic class - integer, float, string
x=1
y=5.1
z=x*y

print(z)
print(type(x))
print(type(y))
print(type(z))

print(x+y)
print("x+y")
#%%
# += executes the numeric operation cycling on the variable
# Known as syntactic sugar - +=, -=, /=, *= ...
i=1
while i<=20:
    if i ==1:
        print("this is the", i, "st x")
    elif i ==2:
        print("this is the",i,"nd x")
    elif i==3:
        print("this is the", i, "rd x")
    else:
        print("this is the", i, "th x")
    print("x=",x)
    x+=1
    i+=1 

x = 1
#%%
# + works with strings
# syntactic sugar works with strings as well
a = "abc"
b = "123"
c = a+b
print(c)
a+=b
print(a)

#%%
#.upper() makes all letters in the string uppercase, vice versa with .lower()
A = a.upper()
print(A)
AA = A.lower()
print(AA)

# in python, cannot use "." in object naming: syntax: object_name.function_method()

#%%
#.capitalize() caps the first letter of the string
#.strip() removes all spaces until the first letter in a string
# String methods can be used as a chain - object_name.function1().function2()
test_string = " hello world!"
cap_string = test_string.capitalize()
cap_string_strip = test_string.strip().capitalize()
upper_string = test_string.upper()
print("test_string:",test_string)
print("cap_string:",cap_string)
print("cap_string_strip:", cap_string_strip)
print("upper_string:", upper_string)


#%%
#String Formatting - f '... {} ...' - basically just add f before the string and plug {} at the input location

username = input("What's ur name?")
greetings = f'Hello {username}, nice to meet you!'
print(greetings)

#Another way - use the {} as a place holder and attach .format() in the end
greetings_2 = 'Hi {}, it is nice meeting you!'.format(username)
print(greetings_2)



#%%
# List - a vector of variables
list_1 = [1,2,3]
print(list_1)
print(len(list_1))


# Python is 0-based indexing - first position is always 0.
# Position slicing syntax: List[start:stop:step]
list_2 = ['a', 'b', 'c', 'd', 'e']
print(list_2[0:5:2])
print(list_2[5:0:-2])

print(list_2[3:]) #print starting from the position 3
print(list_2[:3]) #print until the position 3
print(list_2[::2])

print(list_2[:3] + list_2[3:]) #do not close up on both sides is to avoid overlap of the position 3

# List can be iterated, position: list1[index][index]
# Tuple is to help distinguish itself in a list - list in a list; Tuples cannot be overwritten
# Lists can be overwritten


#%%
# Sets - a list-like object
# Set enforce unique values
# Sets do not mantain ordering

set_1 = {'a','a','b','s','c','c','f'}

print(set_1)

#%%
# Dictionary - creates a matching library
# links a key to a value/variable e.g. student number:name
# Used to rename variable names/columns

dict_1 ={"Lucas":"yj1084", "Rita":"yl4034"}
print(dict_1['Lucas'])

#%% 
#Dates

test_date1 = datetime.datetime(2020,1,20,0,0,0)
print(test_date1)
print(test_date1.year)
print(test_date1.month)
print(test_date1.day)

#date calculation available
time_since_covid = datetime.datetime.now() - test_date1
print(time_since_covid)