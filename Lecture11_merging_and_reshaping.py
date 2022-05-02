# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:59:16 2022

@author: Lucas Jiang
"""

#%%
import pandas as pd

data1 = {"name":["a", "b", "c"], "val1":[1, 2, 3]}
data2 = {"name":["b", "c", "d"], "val2":[4, 5, 6]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#%% Combine data with Merge
"""
Arguments for matching data:
    on = column name
    left_on,right_on = column name, column name
    left_index,right_index = boolean, boolean

Arguments for match logic:
    how = "left" , everything thats on the left (drops right section's elements if not in left)
    how = "right", evrything thats on the right (drops left section's elements if not in right)
    how = "inner" , intersection of the two
    how ="outer" , combination of the two

"""

#%% Conbine data with merge: outer
df_out = df1.merge(df2, on="name", how="outer")
print(df_out)
 #Conbine data with merge: inner
df_in = df1.merge(df2, on="name", how="inner")
print(df_in)

#combine data with merge:more
df_1left = df1.merge(df2, on="name", how="left")
print(df_1left)

#%% Auditing merges
data3 = {"name":["a","a","c"], "val3":[7, 8, 9]}
df3 = pd.DataFrame(data3)

df_1extra = df1.merge(df3, on="name", how="left")
print(df_1extra)
# in this case multiple rows with indeed same name-values, solution
#1. validate
df_1validate = df1.merge(df3, on="name", how="left", validate="one_to_one")

#%%
#2. use assert to check the length of the rows before and after merging
start_len = len(df1)
df_merge = df1.merge(df2, on="name", how="outer")
end_len = len(df_merge)

assert(start_len == end_len), "Unexpected dataframe expansion after merge"


#%%
#3. use indicator to let pandas tell us where each line comes from
df_merged = df1.merge(df2, on="name", how="outer", indicator=True)
print(df_merged)

#We can further filter data with indicator
print(df_merged[df_merged["_merge"] != "both"])

#%% Conbine data with merge: different merge keys
data4 = {"NAMES":["a","b","c"], "val4":[10, 11, 12]}
df4 = pd.DataFrame(data4)

df_lo = df1.merge(df4, left_on="name", right_on="NAMES", how="inner")
print(df_lo)

#%% Combine data with merge: multiple keys
#e.g.
df5.merge(df6, on=["name","month"], how="inner")



#%% combine data with concat
data7 = {"name":["d","e","f"], "val1":[21, 22, 23]}
df7 = pd.DataFrame(data7)

df_concat = pd.concat([df1,df7])
print(df_concat)

#%% Reshaping: wide to long (with stubs)
data = {"student":["A","B","c"],
        "grade2019":[4.00, 3.50, 3.75],
        "grade2018":[4.0, 4.0, 3.5],
        "grade2017":[3.0, 2.0, 3.5]
        }
df = pd.DataFrame(data)

df_wtl = pd.wide_to_long(df, "grade", i="student", j="year")
print(df_wtl)

#%% Reshaping: wide to long (w/o stubs), use df.melt()

data8 = {"student":["A","B","c"],
        "2019":[4.00, 3.50, 3.75],
        "2018":[4.0, 4.0, 3.5],
        "2017":[3.0, 2.0, 3.5]
        }
df8 = pd.DataFrame(data8)
df_melt = df8.melt(id_vars="student", value_vars=None, var_name="year", value_name="grade")
print(df_melt)

#%% Reshaping: long to wide, use pivot
df_pivot = df_melt.pivot(index="student", columns="year", values="grade")
print(df_pivot)

#Reshaping guide
# https://pandas.pydata.org/docs/user_guide/reshaping.html