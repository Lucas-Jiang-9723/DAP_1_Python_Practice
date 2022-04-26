# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:47:48 2022

@author: Lucas Jiang
"""

#%% Deal with errors
x = 10
y = 0
z = x / y
#   method 1 leave it as is : the traceback gives message
#%%
#   method 2 use assert function if true, continue, if false, holds the program and prints the error message
#   continues if true, return error message if false
x = 10
y = 0
assert(y != 0), "Error: y cannot be 0"
z = x / y



#%% method 3
#   Capture the error using a try/except block, and then proceed with our program without halting
x = 10
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Error: y cannot be 0")


#%% Chain except statements together, just like elif and conclude with a catch-all except at the end
#   NoteL the last except block will capture all tracebacks, and is not generally a good practice

x = 10
y = [0]
try:
    z = x / y[0]
except ZeroDivisionError:
    print("Error: y cannot be 0")
except IndexError:
    print("ErrorL the length of list y is not correct")
except:
    print("something else went wrong...")

#%% combining assert with isinstance
def string_fixer(s):
    s = s.lower().strip()
    if s.startwith("a"):
        return "it's an a!"
    else:
        return "it's not an a!"

a = isinstance("Hello world!", str)
b = isinstance("Hello world!", int)
print(a)
print(b)

class MyClass():
    pass
my_instance = MyClass()
print(isinstance(my_instance, MyClass))

#%% combine
def string_fixer(s):
    assert(isinstance(s,str)), "string_fixer requires string argument"
    
    s = s.lower().strip()
    if s.startwith("a"):
        return "it's an a!"
    else:
        return "it's not an a!"

string_fixer(42)

#%% another eg to solve the following issue - legit but the result is nonsense

def math_some_numbers(a,b):
    val = (a + b) * 2
    return val

print(math_some_numbers(10, 20))
print(math_some_numbers("Hello", "World"))

#%% Solution
import numbers

def math_some_numbers(a, b):
    assert(isinstance(a, numbers.Number) and 
           isinstance(b, numbers.Number)), "Must pass in numeric arguments!"
    val = (a + b) * 2
    return val

print(math_some_numbers(10, 20))

print(math_some_numbers("Hello", "world"))



#%% Simulations Schelling model
# 1. An agent class to represent each individual actor in the game
#    1. how to move
#    2. how to decide if they are happy
#    3. how to look at their neighbors
class Agent():
    def __init__(self):
    #needs to know its color and its same preference
        pass

    def move(self):
        # decide if it wants to move
        # move to new position if it does
        # uses the self.am_i_happy method
        pass





# 2. a world class holds knowledge of the grid and agents
#    1. how to set everything up
#    2. how to provide info to agents
#    how to report on the state of the simulations
#    how to run the simulation

class World():
    def __init__(self):
        # sotres the grid as a container of some sort
        # calculates how many agents there should be 
        # initializes agents in starting locations
        # uses the build_grid and, build_agents, and init_world methods
        pass
    
    def build_grid(self):
        #sets up the word agents can move in, returning a dict
        pass

    def build_agents(self):
        # generates the list of agents that can be iterated over
        pass
    
    def init_world(self):
        # sets up the starting conditions of the world
        pass
    
    def find_vacant(self):
        #find a list of empty patches and returns a random one
        pass

    def report_integration(self):
        # generates a report at the end of the current round
        pass
    
    def repot(self):
        # generate the final report at model end
        pass
    
    def run(self):
        # executes the model as set up
        pass
    

world = World()
world.run()



#%%