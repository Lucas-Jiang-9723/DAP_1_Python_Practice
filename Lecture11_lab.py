import pandas as pd

#combine these three dataframes so that the result is a single
#dataframe with the columns "date", "place", "value1", "value2",
#with the date columns being datetime objects that run from
#1/2020 to 10/2021, without modifying any starter code

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

data3 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01', '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

df_val1 = pd.DataFrame(data1)
df_val2 = pd.DataFrame(data2)
df_val3 = pd.DataFrame(data3)
#%% Data Overview
print(df_val1)
print(df_val2)
print(df_val3)

#%% df1

# convert to datetime
# df1 needs wide to long
pd.to_datetime(df_val1["date"])
df_val1_f = pd.wide_to_long(df_val1, "place", i="date", j="year")
print(df_val1_f)

#%% df2
# convert to datetime, pd.to_datetime(df["name"])
pd.to_datetime(df_val2["date"])

# set date as index
df_val2_f = df_val2.set_index("date")
df_val2_f["place"] = df_val2_f["place"].str.replace("place","")
print(df_val2_f.dtypes)
print(df_val2_f)
#%%Solution

# 1. 更改日期格式
# 2. 创建val1 & Val2
# 3. 
