# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:18:48 2022

@author: Lucas Jiang
"""

#%% Load data
import pandas as pd
import os

base_path = r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Spring 2022\DPPP_Python\Lecture\Lecture12 Groupby"
file_name = r"diamonds.csv"

full_path = os.path.join(base_path, file_name)

diamonds = pd.read_csv(full_path)

#%% df.groupby(var).mean() groups data by the variable name and calculates the mean of other variables under the same var
#   remember to reset the index to avoid groupby setting clarity as the index
diamonds_byclarity = diamonds.groupby("clarity").mean().round(2).reset_index()
print(diamonds_byclarity)

#%% df.sort_values(var) sorts the dataframe according to value of the var
#   Keywarg - accending default to be true
diamonds_byclarity.sort_values("clarity")
print(diamonds_byclarity)
#%% customize sorting order
clarity_order = ['I3', 'I2', 'I1', 'SI2', 'SI1', 'VS2', 
                 'VS1', 'VVS2', 'VVS1', 'IF', 'FL']

#pd.Categorical(column to be sorted by, order wanted to be applied, ordered=True)
category = pd.Categorical(diamonds_byclarity["clarity"], 
                          categories=clarity_order, 
                          ordered=True)
#assign the categorical order to the target sorting column in the df
diamonds_byclarity["clarity"] = category
diamonds_byclarity.sort_values("clarity")

print(diamonds_byclarity)


#%%



#%% group.max() gives out the maximum value of each group
#   more flexible alternative group.apply(lambda g: g.max())