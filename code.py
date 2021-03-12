from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

data = requests.get(url)

soup = bs(data.text, "html.parser") 
table = soup.find_all('table')

tempList = []
trTag = table[4].find_all('tr')

for tr in trTag:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

names = []
radius = []
mass = []
distance = []

tempListLen = len(tempList)

for i in range(1,tempListLen):
    names.append(tempList[i][0])
    radius.append(tempList[i][9])
    mass.append(tempList[i][8])
    distance.append(tempList[i][6])

df = pd.DataFrame(list(zip(names,radius,mass,distance)),columns=['Name','Radius','Mass','Distance'])
df.to_csv('browndwarfs.csv')