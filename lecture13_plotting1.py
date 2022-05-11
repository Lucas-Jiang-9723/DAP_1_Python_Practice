# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:07:41 2022

@author: Lucas Jiang
"""

#%% library imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#%% sample data creation
x = range(300)
y=np.random.choice([-1,0,1], 300)
y = np.cumsum(y) # random walk

#%% MatPlotLib Basic Plot 
# fig: one object representing the canvas that all plots show on
# axL one plot axis that goes on a figure
fig, ax = plt.subplots() #figure and axis using plt.subplots()
ax.plot(x, y, label="basic plot1")
# To explicitly render a plot rather than waiting for the interpreter to assume we want it, call fig.show()
fig.show() # better do this when everything is done 

#%% Controlling colors and lines

fig, ax = plt.subplots()
ax.plot(x, y, color="red", linestyle="solid")
fig.show()

fig, ax = plt.subplots()
ax.plot(x, y, color="black", linestyle="solid", marker="o", linewidth=2,
        markersize=5, markerfacecolor="red", markeredgecolor="navy")
fig.show()
#some easier argument:
    #"r" = red, "-" = solid, "--" = dashed
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

#%% Format Strings

#%% Legends and line labels
fig, ax = plt.subplots()
ax.plot(x, y, "r-", label="This is a label")
ax.legend(loc="best")
fig.show()
#%% Multiple lines
#   simple, call ax.plot again
fig, ax = plt.subplots()
ax.plot(x, y, "r-", label="forward line 1")
ax.plot(x, y[::-1], "b-", label="backward line 2")
ax.legend(loc="best")
fig.show()

#%% Python Review
"""
fig and ax are instances of MatPlotLib "figure" and "axis" objects
plt is the MatPlotLib module
ax.plot/axis.legend: plot/legend is a method of an axis
"""

#%% Labels
fig, ax = plt.subplots()
ax.plot(x, y, "g-")

ax.set_ylabel("This is the y axis")
ax.set_xlabel("This is the x axis")
ax.set_title("This is the title")

fig.show()


#%% Spines and Lines
fig, ax = plt.subplots()
ax.plot(x, y, "b-")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.axvline(150, color="k", linestyle=":")
ax.axhline(5, color="k", linestyle=":")
fig.show()
#%% MatPlotLib axis vs module objexts

#2 ways to matplotlibs:
    #1. DO NOT USE
plt.plot(x, y, "b-")
    #2. USE THIS
fig, ax = plt.subplots()
ax.plot(x, y, "b-")

#%% Plotting with Pandas 
plot_1 = pd.DataFrame({"values_x":x, "values_y":y})
print(plot_1)
plot_1.plot(x="values_x", y="values_y")

# combination - capture the pandas df plot and put into matplotlib to add a dashed line
ax = plot_1.plot(x="values_x", y="values_y")
ax.axvline(150, color="k", linestyle=":")
#%% multiple plots
plt.subplots(2,2)