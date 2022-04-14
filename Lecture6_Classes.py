# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:32:02 2022

@author: Lucas Jiang
"""

#%% 

#   e.g.1- Class with 3 properties
#   Useless but working :)
class Class1():
    a = 10
    b = 20
    x = a + b

instance_1 = Class1()
print(instance_1.x)
#%% Customizing class instances
#   e.g.2
#   The __init__ leading and trailing double underscore measn this is a reserved method
#       which means that python classes know to look for this method and treat it in a certain way
#   Self => It is named self purely by concvention, its a normal positional argument that
#       can technically be named anything
#       The 1st postioning argument under the hood is always reserved for a pointer back to the instance
#   This is how a method knows the value of the instance

class Class2():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b
#   x is the instance in this case


print(Class2(10,10).x)
print(Class2(20,20).x)



#%%
print(type(Class2(20,20)))


#%% Adding methods to a class
#   E.g. 3 - Create a class that starts with values for the number of bedrooms, bethrooms, and the square footage
#   Add a method that uses these three values to calculate a home price
#   Then add a method that randomly pickes a markup for the neighborhood and modifies the result

from numpy import random

class HouseValues():
    def __init__(self, num_bedrooms, num_bathrooms, sqft):
        # needs three values: num bedrooms, num bathrooms, sqft
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.sqft = sqft
        
    
    def estimate_value(self):
        # use an equation of questionable accuracy that I found on a randome
        # website to estimate the value based on those three parameters
        # add 10% per number of bedrooms to 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        # add 5% per num of baths over 1
        bath_mod = ((self.num_bathrooms - 1) * 0.05) + 1
        
        neighbor_mod = self.pick_a_neighborhood()
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod * neighbor_mod
        print(f"I estimate this house will be worth ${round(self.value,2)}")
       
    def pick_a_neighborhood(self):
        # randomly pick a modifier to multiple the value estimate by
        value = random.normal(1, 0.1)
        if value > 1.2:
            print(f"This neighborhood is expensive - {round(value,2)}")
        elif value > 1:
            print(f"aeverage neighborhood - {round(value,2)}")
        elif value < 1:
            print(f"Cheap neighborhood - {round(value,2)}")
        return value

house1 = HouseValues(2, 2, 950)
house2 = HouseValues(1, 1, 700)
house1.estimate_value()
house2.estimate_value()