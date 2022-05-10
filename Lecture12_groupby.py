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


#%% Group by multiple categories
diamonds[">1ct"] = diamonds["carat"].map(lambda c: 1 if c > 1 else 0)
diamonds_byclarity_byct = diamonds.groupby(["clarity", ">1ct"]).mean().round(2)


#%% Groupby is itself an object
test_group = diamonds.groupby("clarity")
print(test_group.groups) # the groups show that inside the groupby class, the values are stored as dictionaries

# We can look for the data of a specific category/variable using get_group()
print(test_group.get_group("I1"))

# df.describe() is also a groupby method - shows descriptive info
print(test_group.describe())

# basic data exploration
print(test_group.apply(lambda g: g["price"].max()))

#%% Strings in DataFrames
diamonds_1 = diamonds
diamonds_1["cut"].str.upper()
diamonds_1["cut"].str.replace("Ideal", "ideal")

#%% Missing Values df.dropna() keywarg default to value: how = "any"
diamonds_1.dropna(axis=1, thresh=3) # only keep the columns where 3 or more cells are NaN
diamonds_1.dropne(how = "all") # drops if all cells are NaN

# we can fill na values using df.fillna()
diamonds_1.fillna(0)
diamonds_1.fillna(method = "backfill") # - takes the value below it and fills in
# specify what value to fill in na depending on the column name
diamonds_1.fillna({"col1":100, "col2":200})
# fill one column's missing values from elements from another column: df["col1"].fillna(df["col2"])
diamonds_1["cut"].fillna(diamonds_1["clarity"])
#%% group.max() gives out the maximum value of each group
#   more flexible alternative group.apply(lambda g: g.max())