# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:15:46 2022

@author: Lucas Jiang
"""
#%% Course material - libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#%% Showing, Saving and Clearing
fig.show()
fig.savefig("plot.png")
fig.clear()
#%% sample data creation
x = range(300)
y=np.random.choice([-1,0,1], 300)
y = np.cumsum(y) # random walk

#%% Dual-Y Axis Plots
fig, ax =plt.subplots()
ax.plot(x, y, "b-", label="blue line")
ax.legend(loc=9) #9 is upper center

y_2 = y[::-1]*100
ax2 = ax.twinx() #build another axes where x axis is the same
ax2.plot(x, y_2, "r-", label="y_2 line")
ax2.legend(loc=9)
fig.show()
"""
what the above essentially does is simply layer another axis on the first one - can cause problem when trying to add legend as we saw
"""
#solution: Add a duplicate of the ax2 line, but with NaN as the values to the plot
fig, ax =plt.subplots()
ax.plot(x, y, "b-", label="y value")
ax.plot(np.NaN, "r-", label="y_2 value")
ax.legend(loc="lower center")

# cheat a little by layering a second axi, creat a blank plot in axis one but add legend
ax2 = ax.twinx()
ax2.plot(x, y_2, "r-", label="y_2 value")
fig.show()

#Solution2: just use pandas - I prefer this
df = pd.DataFrame({"values_y1":y, "values_y2":y_2})
ax = df.plot(secondary_y="values_y2")

#%% Multiple Sublplots
fig, ax = plt.subplots(2,2) # row, column
"""
In this scenario, ax is no longer an object, but it is a nested list format now
"""

#%% example
def random_walk_y(obs):
    y = np.random.choice([-1,0,1], obs)
    return np.cumsum(y)

fig, axs = plt.subplots(2,2)
axs_flat = [s for sublist in axs for s in sublist]
ys = [random_walk_y(300) for _ in range(4)]

# do this when the len of ax and y are equal
for ax, y in zip(axs_flat, ys):
    ax.plot(x, y)
    ax.set_ylim(-20,20) #to set all y axis the same
    
#%% Multiple plots: pandas
df = pd.DataFrame({"values_y1":random_walk_y(300),"values_y2":random_walk_y(300),
                   "values_y3":random_walk_y(300),"values_y4":random_walk_y(300)})
df.plot(subplots=True)

#%% Other Plot Types


#%% Scatter Plots
fig, ax = plt.subplots()
ax.plot(range(100), random_walk_y(100), linestyle="", marker=".", markersize=5)
fig.show()
# alternative
fig, ax = plt.subplots()
ax.scatter(range(100), random_walk_y(100), s=2) #s for size
fig.show()

#%% Bar Plots
x = [2, 4, 6, 8, 10]
y = [1., .2, .4, .7, .9]
fig, ax = plt.subplots()
ax.bar(x, y)

#%% Box Plots
x = [np.random.normal(10, 2, 100),
     np.random.normal(11, 1, 100),
     np.random.normal(20, 4, 100)
     ]

fig, ax = plt.subplots()
ax.boxplot(x)
#%% Seaborn - a convenient package that essentially use matplotlib
df = pd.DataFrame(np.array(x).T, columns=["first", "second", "third"])
print(df.head())

sns.set()
sns.boxplot(data=df)
# we can combine seaborn with plot operations

#%% Seaborn - grouped box plots
tips = sns.load_dataset("tips")
print(tips.head())
ax = sns.boxplot(x="day", y="total_bill",
                 hue="smoker", palette=["m","g"],
                 data=tips)
ax.set_ylabel("Total Bill")
ax.set_xlabel("Day")
ax.set_title("Tips left by diners")