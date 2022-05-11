#%% import libraries
import matplotlib.pyplot as plt
import pandas as pd
import datetime
#%%
# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical
# lines to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   March 2020 - January 2021 (technically not billed a recession but we'll include it anyway!)

#%% file loading
df = pd.read_csv(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Spring 2022\DPPP_Python\Github_Repo\DAP_1_Lecture_Lab_Repo\UNRATE.csv",
                 parse_dates=['DATE'])



#%%
recessions = [(datetime.datetime(2001, 3, 1),  datetime.datetime(2001, 11, 1)),
              (datetime.datetime(2007, 12, 1), datetime.datetime(2009, 6, 1)),
              (datetime.datetime(2020, 3, 1),  datetime.datetime(2021, 4, 1))]
#%% plotting data

fig, ax = plt.subplots()
ax.plot(df["DATE"], df["UNRATE"], "b-", label="Unemployment Rate")
ax.set_xlabel("DATE")
ax.set_ylabel("Unemployment Rate")
for tpl in recessions:
    ax.axvspan(tpl[0], tpl[1], color="gray", alpha=0.5)
ax.legend(loc=1)
fig.show()
#%% 
fig, ax = plt.subplots()
ax.plot(df["DATE"], df["UNRATE"], "b-", label="Unemployment Rate")
ax.set_xlabel("DATE")
ax.set_ylabel("Unemployment Rate")
ax.axvspan(recessions[0][0],recessions[0][1], color="gray", alpha=0.5, label="Recession")
ax.axvspan(recessions[1][0],recessions[1][1], color="gray", alpha=0.5)
ax.axvspan(recessions[2][0],recessions[2][1], color="gray", alpha=0.5)
ax.legend(loc=1)
fig.show()

#%% Solution

for start, end in recessions:
    ax.axvspan(start, end, alpha=0.4, color="gray")