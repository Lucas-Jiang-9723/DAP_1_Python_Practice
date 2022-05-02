# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:05:05 2022

@author: Lucas Jiang
"""

#%% Contents for today
"""
1. Defining Path Statements
2. Reading from CSV
3, Basic Exploration
4. Dates
5. Renaming
6. Subsetiing by conditionals
7. Applying functions using map, apply, and applymap
"""


#%% 1. Path statements

#1. Absolute Path
# The plain path from the very beginning
# In larger project with multiple files from different locations, more useful
abs_path = r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Spring 2022\DPPP_Python\Lecture\Lecture10 Pandas 2\GDPC1.csv"
# the "r" makes a raw string. it treats "\" as string rather than separating symbol
print(r"Hello World! \n How are You? ")
# \n indicates break and start in a new line
print("Hello World! \nHow are you!")


#2. Relative Path
# Just the file name relative to the working directory
# Requires the wd to be the location where the file is at
# Can setup wd beforehand
rel_path = "GDPC1.csv"

#%% os library and join relative path

# os.path.join can join the srings to form a proper path 

import os
base_path = r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Spring 2022\DPPP_Python\Lecture\Lecture10 Pandas 2"
path = os.path.join(base_path, "GDPC1.csv")


#%% 2. Reading from CSV
#   use pandas
import pandas as pd
df_1 = pd.read_csv(path)

#%% 3. Basic df exploration

# df.head()/.tail() by default output the top/bottom 5 rows if no arguments given
print(df_1.head(6))

print(df_1.tail())

# df.shape tells the size: (#rows, #columns)
print(df_1.shape)

# df.dtypes shows the data type of each variable in the df
print(df_1.dtypes)

#%% 4. Dates
# in the example the date is not a date object. We need to convert the string into date

# 1. pd.to_datetime(df["name"]), takes any argument and converts it into date type(will try its best)
#    this method works even with y,m,d in separate columns in the df, just pass them all into this method
df_1["DATE_1"] = pd.to_datetime(df_1["DATE"])
print(df_1.dtypes)

# 2. We can also handle this during the reading csv process
#    Using the read_csv , parse_dates argument
df_2 = pd.read_csv(path, parse_dates=["DATE"])
print(df_2.dtypes)

#%% 5. Renaming
# use a library and a df.rename(name_dict, axis= argument)to rename the column of the df
# axis=1 ??
# rename will rename index(row) and the columns
# axis = 1 indicates renaming along the column (horizontally)
# axis = 0 indicates renaming along the row (vertically)
# axis argument works in a lot of methods e.g. df.mean(axis = 0/1)
names = {"DATE":"date" , "GDPC1":"gdp"}
df_1 = df_1.rename(names, axis=1)

# another alternative: use the columns keywarg
df_1 = df_1.rename(columns = names)


#%% 6. Subsetting by conditionals

#1. e.g df[df[var] > 100]
#   what this really does is returning the result of conditional booleans that is "True"
print(df_1[df_1["gdp"] > 10000])

#e.g.
import datetime as dt
start_date = dt.datetime(1999, 1, 1)
print(df_1[df_1["DATE_1"] > start_date])

# e.g. when testing multiple conditions, must use () to wrap each boolean tests
print(df_1[(df_1["DATE_1"] > start_date) & (df_1["gdp"] > 10000)])


#%% 7. Function applied to each cell in one column
# map() - simplest; it works independent of the cells around the cell, each cell is treated separately
# df[var].map() applies a function to values in one column, one at a time

# argument x takes on each value of a cell only

import statistics as st

#e.g.
def double(x):
    return x * 2
df_1["gdp"] = df_1["gdp"].map(double)
print(df_1)

# apply()
# df.apply(func) - applies a function to values in every colun, one entire column at a time
# this gives us the ability to access the values around the cell that we are operating on: e.g. zscore

# argument x takes on the value of one entire column
# Apply tries column by column, so if not all columns are numeric, do not use it, use the function directly instead
def zscore(x):
    print(x)
    return (x - x.mean()) / x.std() #issue need error check

#    return (x - st.mean(x)) / st.std(x)
# here x makes sense only if it's an entire column
df_1["gdp"] = df_1["gdp"].apply(zscore)
print(df_1)

# applymap() 
# df.applymap(func) - applies a function to values in all columns, one cell at a time

# argument x takes on each value of a cell
df_1 = df_1.applymap(double)
print(df_1)


#%%
def zscore(x):
    return (x - st.mean(x)) / st.std(x)

list1 = [1, 2, 3, 4, 5]

zscore(list1[2])
#%%
"""
copy a new df from the original df and add a new column without impacting the original one
use assign()
"""
