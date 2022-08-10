
import requests
from bs4 import BeautifulSoup
import pandas as pd

request = requests.get('https://news.daum.net/')

soup = BeautifulSoup(request.text, 'html.parser')

l = []
index = 0
for item in soup.find_all('div', class_ = 'item_issue'):
    link_txt = item.find('a')
    url = link_txt['href']
    print(index, url)
    l.append([index, url])
    index+=1

df = pd.DataFrame(l, columns=['index', 'url'])
df.to_excel('daum_news.xlsx', index=False)