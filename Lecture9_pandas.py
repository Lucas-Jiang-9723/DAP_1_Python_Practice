# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:48:23 2022

@author: Lucas Jiang
"""

#%% import statements three ways

#1.
import pandas
pandas.DataFrame

#2. Most common by convention ************
import pandas as pd
pd.DataFrame

#3.
from pandas import DataFrame
DataFrame

#%% e.g. first df

data = {"month": [1, 2, 3],
        "unemp_il": [5.6, 5.7, 5.8],
        "unemp_wi": [6.1, 6.0, 6.1],
        "gdp_il": [6, 6, 7],
        "gdp_wi": [4, 5, 4]}

#.dataframe() is the class object being called
# data is the argument pased into the dataframe classes__init__ method
df_1 = pd.DataFrame(data)
print(df_1)
#%% Subsetting a dataframe
#   select by column
#   by index(row)
#   by column and index
#   by conditionals


#%%
# a column in a dataframe is called a series 

#%%
#1. Select by column
#note: Use [] and pass string in

print(df_1["month"])


#note: double-square brackets bcuz: we are passing a list in the df[]
print(df_1[["month","gdp_il"]])

#alternative
list_1 = ["unemp_il", "unemp_wi"]
print(df_1[list_1])


# Select range of columns 

df_1.loc[:,range[1,2]]
#%% e.g. conditionals in list comprehension
print(df_1[[col for col in df_1.columns if col.endswith("il")]])

#%% Applying operations over columns
#   We can apply nearly ANY function that takes a list-like object to a column

import numpy as np
print(np.mean(df_1["unemp_il"]))

# in most cases dataframe also have its own methods
print(df_1["unemp_il"].mean())




#%% select rows in df

# selecting using slicing notation - not recommended (ambiguous)
print(df_1[1:])

# we can overwrite the row name using index class
df_1.index = ["row_a", "row_b", "row_c"]
print(df_1)

#   Use loc for location   (using row names)
print(df_1.loc[["row_a", "row_c"]])

#   Use iloc for index location (using row position, not the name)
#   double square brackets as well if multiple rows
print(df_1.iloc[2])

print(df_1.iloc[[1, 2]])


#%% Select by column and row(index)

#   Note: Rows Go First! Columns Next!
#   Use .loc

combo = df_1.loc[["row_a","row_c"], ["gdp_wi","gdp_il"]]
print(combo)

#   Use .iloc
combo_2 = df_1.iloc[[0,1],[1,2]]
print(combo_2)

#   Using iloc or loc to select by rows
#   Use : to select all rows by default
df_2 = df_1.loc[ :, ["unemp_il", "unemp_wi"]]
print(df_2)


#%% View a df vs Full copy of a df
#   Has sth to do with the memory management

#In concept if we subset from a df, the console copies part of the df and pastes to a new location in the harddrive
# but in this following case, its creating a view which "shows" part of the original df
#   The console does not know if we want to modify the original df or try to copy and paste the subset and then modify

# test1 is a view - don't do this
test1 = df_1[["unemp_il", "unemp_wi"]]
test1["il_rescaled"] = test1["unemp_il"] * 0.1
# Solution add .copy()
test3 = df_1[["unemp_il", "unemp_wi"]].copy()
test3["il_rescaled"] = test3["unemp_il"] * 0.1


# test2 is a full copy - downside: may cause problem with a large dataset
# On the contrary, using loc is actually copying and pasting a subset to a new location in the hard drive
test2 = df_1.loc[:,["unemp_il", "unemp_wi"]]
test2["il_rescaled"] = test2["unemp_il"] * 0.1


#%%