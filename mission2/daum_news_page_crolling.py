
import requests
from bs4 import BeautifulSoup

request = requests.get('https://news.v.daum.net/v/20220810005210818')

soup = BeautifulSoup(request.text, 'html.parser')

title = soup.select_one('#cSub > div > h3').text
print(title)

date = soup.select_one('#cSub > div > span > span:nth-child(2) > span').text
print(date)

body = soup.select_one('#harmonyContainer > section').get_text().strip()
print(body)
