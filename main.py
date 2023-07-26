from bs4 import BeautifulSoup
import pandas as pd

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

titles = soup.find_all("h3", {"class": "ipc-title__text"})
movies = []
title = []
titles = titles[1:251]
for t in titles:
    title.append(t.text)

years = [i.text for i in soup.select('.cli-title-metadata span:first-child')]

durations = [i.text for i in soup.select('.cli-title-metadata :nth-child(2)')]

rate = [i.text for i in soup.select('.cli-title-metadata :nth-child(3)')]

ratings = [i.text for i in soup.select('.ipc-rating-star--imdb')]

df = pd.DataFrame({"title": title, "year": years[0:250], "duration": durations[0:250], "rate": rate[0:250], 'rating': ratings[0:250]})
df.to_csv('imdb_top250.csv',index=False)
