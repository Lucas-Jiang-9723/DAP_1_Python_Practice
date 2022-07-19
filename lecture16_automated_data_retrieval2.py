# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:57:14 2022

@author: Lucas Jiang
"""


#%% libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#%% HTML Basics
"""
* Makes the structure of websites
* A website consists of HTML elements
    * An open (start) tag
    * Some attributes
    * Content
    * A close (end) tag
"""


#%%
with open(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Spring 2022\DPPP_Python\Lecture\Lecture16 Automated data retrieval2\test_page.html",
          "r") as page:
    text = page.read()
    
soup = BeautifulSoup(text, "lxml")
# lxml is an external resource used by browsers to parse HTML, if having issues with using it here, use the default Python parser ,"html.parser"
# the soup object is the website content, parsed into an easy to use reference
#%% searching a "soup" object
tag_all_p = soup.find_all("p") #find all tags with p and returns a list
# can input argument i.e. href="https://harris.uchicago.edu/" as criteria so that both conditions are matched
print(tag_all_p)

# if not exact match
tag_a = soup.find_all("a", href=lambda h: "uchicago" in h) 


tag_first_a = soup.find("a") 
#finds the first tag with a and return a single tag
print(tag_first_a)

tag_first_a.attrs # returns a library in which the key is the href, the value is the content
tag_first_a.contents # returns Harris School
tag_first_a.has_attr("href") # validates if there is an attribute href in the tag
tag_first_a.parent # goes out to the next level
#%% example
url = 'http://maktaba.tetea.org/exam-results/FTNA2015/S0206.htm'
path = r"c:\users\Lucas Jiang\desktop\grades.csv"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml") #or hteml.parser

# parsing a table
table = soup.find("table")
table.find_all("tr")[24].find_all("td")
#%%
unparsed_rows=[]
for row in table.find_all("tr"):
    td_tags = row.find_all("td")
    unparsed_rows.append([val.text for val in td_tags])

unparsed_rows[25]
# the whole grade row is one cell in the case above , need to fix this
def row_parser(row):
    if row[4] == "Absent":
        row = row[:4] + ["Absent"]*17
    return ",".join(row)
parsed_rows = [row_parser(row) for row in unparsed_rows[24:152]]
#%%
# build our own table to put in the data
header = 'CNO,Repeat,Name,Sex,CIV,HIST,GEO,EDK,KIS,ENG,FRN,PHY,CHEM,BIO,COMP,MATH,FOOD,COMM,BKEEPING,GPA,CLASS'
parsed_rows.insert(0, header)

document = "\n".join(parsed_rows)
with open(path, "w") as ofile:
    ofile.write(document)
# "w" : text only
# "wb": write in binary format
# "r": read
# "r": read in binary format
# "a": append
