#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

fig, ax = plt.subplots()
grouped = df.groupby('species')
colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}

for key, group in grouped:
    group.plot(x='sepal_length', y='petal_length',
               ax=ax,
               kind='scatter',
               color=colors[key],
               label=key.capitalize())

leg = ax.legend()
leg.set_title('species')
plt.show()

#recreate this plot in Seaborn!

#%%
print(df.head())
ax = sns.scatterplot(x="sepal_length", y ="petal_length", 
                     hue="species", palette=["r","b","g"],
                     sizes=8,data=df.rename(columns={"v":"V"}))


#%%
fig, ax = plt.subplots()
ax = sns.scatterplot(x="sepal_length", y ="petal_length", 
                     hue="species", palette=["r","b","g"],
                     sizes=8,data=df.rename(columns={"v":"V"}), ax=ax)