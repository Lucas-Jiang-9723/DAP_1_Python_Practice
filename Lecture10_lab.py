#%%
import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

df = pd.read_csv(url_to_csv)
print(df)
#%%
#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values?  How would you find the mean values
#   per type of flower (you don't actually have to implement this - we
#   will cover it next week)

print(df.species.unique())

# mean and median of each column
for col in range(0,4):
    print(df.iloc[:,col].mean())
    print(df.iloc[:,col].median())

# mean values for each type of flower


#%%
#2. using one line of code, multiply every value by 100
print(df)
df.iloc[:,range(0,4)] = df.iloc[:,range(0,4)]*100
print(df)

num_cols = df.columns[:-1]
df[num_cols] = df[num_cols].applymap(lambda v: v*2)


#%%
#3. subset the data so only virginica flowers remain
df_vg = df[df["species"]=="virginica"]
print(df_vg)

#%%

#4. create a new column named "petal_area" which is equal to the length
#   times the width
df["petal_area"] = df["petal_length"] * df["petal_width"]
print(df)