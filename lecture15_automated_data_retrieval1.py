# -*- coding: utf-8 -*-
"""
Created on Mon May 16 19:10:49 2022

@author: Lucas Jiang
"""

#%%
import pandas as pd
import datetime

import pandas_datareader.data as web
from pandas_datareader import wb

import requests
#%% Broad Categories of Web Scraping:
    # Using a data API
    # Accessing a file that is directly part of the URL
    # Parsing data out of the html of a website

#%% Pandas DataReader: FRED
#   Series name is the end of the URL
start = datetime.date(year=2000, month=1, day=1)
end = datetime.date(year=2010, month=12, day=31)
series = "ILUR"
source="fred"

df1 = web.DataReader(series, source, start, end) # this is the only step that goes online
print(df1.head())


# series can be a string or a list of strings
series2 = ["ILUR", "WIUR", "MIUR"]
df2 = web.DataReader(series2, source, start, end)
#%% Pandas DataReader: World Bank
# Series name again is part of the URL
indicator1 = "NY.GDP.MKTP.CD"
country1 = "CL"

df3 = wb.download(indicator=indicator1,
                  country=country1,
                  start=2000, end=2010)
print(df3.head())

#Country can be a list of strings as well
country2=["CL", "AR", "BR"]
df4 = wb.download(indicator=indicator1,
                  country=country2,
                  start=2000, end=2010)
print(df4.head())
df4.reset_index()["country"].unique()
#%% Introducing requests: PDF document
url = 'http://standupeconomist.com/pdf/misc/interstellar.pdf'
response = requests.get(url)
# response:
    # contains info about the search (e.g. response code)
    # contains the contents of the headers sent back and forth
    # contains the acutla data that makes up the web page
data = response.content  # this is a binary content, and not readable text


    
#%% Aside: Contexxt management
with open(r'c:\users\jeff levy\desktop\interstellar.pdf', 'wb') as ofile:
    ofile.write(data)
    # closes automatically when indenting is stopped
ofile = open(r'c:\users\jeff levy\desktop\interstellar.pdf', 'wb')
ofile.write(data)
ofile.close()
#%% Responsible automatic data retrieval
# Do the terms of service forbid it?
# Does the robots.txt forbit it?
# How many times does your code query a website?
# How fast is your code running its queries?
# Is it a big website, that can handle a large load, or a small website that you might create problems for ?
# How many times will your code be run