#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup

#%% check terms of service or robot.txt


#%% Web Page -> Table -> Rows -> Cells

url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"
path = r"c:\users\Lucas Jiang\desktop\music.csv"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
#%%
tables = soup.find_all("table")
print(len(tables))
print("The Beatles" in tables[0].text)


# there are both th tags and td tags, need to find both
table = tables[0]
rows = table.find_all("tr")
cells = [r.find_all(lambda c: c.name in ["td", "th"]) for r in rows]

#from row content to csv contents
text = [[t.text.strip().replace("\n","") for t in c] for c in cells]
print(text[1])
text_rows = [",".join(t) for t in text]
text_body = "\n".join(text_rows)

#%% output
with open(path, "w") as ofile:
    ofile.write(text_body)