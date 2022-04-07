# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:33:11 2022

@author: Lucas Jiang
"""

#%% Booleans
#   Python is case sensitive - True & False
value_1 = True
print(value_1)

#%% "in" in Booleans
#    Simply checks if some element is in something
list_1 = ["a","b","c","d","e"]

print("z" in list_1)
print("z" not in list_1)


#%% string methods with Booleans
#   .startswith() checks if the string starts with a letter; similarly, .endswith()
#   .isnumeric() checks if the item is numeric;
str_1 = "Hello world!" 

print(str_1.startswith("H"))
print(str_1.isnumeric())

#%% if statement
#   if we want the 2nd statement to be tested even if the 1st statement is true,
#   we should write 2 statements 
#%% for loops - range - default begins with 0
for i in range(5):
    print(i)
#%% some instructions in loops
#   break - immediately exits the current loop
#   continue - immediately goes to the next iteration of the current loop
list_2 = ["a","b","c","d","e"]
for letter in list_2:
    if letter == "d":
        print("I found the c.")
        break
    else:
        print("still not what i want...")

for letter in list_2:
    if letter == "d":
        continue
    else:
        print("I see the", letter)
    print("end of this iteration",letter)
print("Where is the d though?")

#%% List Comprehensions
#   [f(v) for v in starting_list if <condition>]
#   The output of a list comprehension must be a list; same with dictionary comprehension
#   Without the if condition, it's a mapping comprehension
#   With the if condition, it's a filtering comprehension

#%% Dictionary iteration
dict_1 = {"a":100,"b":200, "C":300}

for key in dict_1.keys():
    print("the key is:",key)

for value in dict_1.values():
    print("the value is:",value)

for key in dict_1.keys():
    print("The value that matches with the key--", key, "--is",dict_1[key])

for key,value in dict_1.items():
    if value == 200:
        print(key)

for item in dict_1.items():
    print(item)
#%% Interlude
#   assigning values, the numbers of items on each side must match strictly (unpack notation)
x,y,z = [1,2,3]
print(x,y,z)

#%% Dictionary Comprehensions
#   new_dict = {f(key):f(value) for key, value in start_dict.items()}

dict_2 = {key.upper():value*2 for key,value in dict_1.items()}
print(dict_2)

dict_3 = {key.upper():None for key in list_1}
print(dict_3)

#%%
