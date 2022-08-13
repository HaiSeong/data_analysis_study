
import requests
from bs4 import BeautifulSoup

def detail_info(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    title = soup.select_one('#cSub > div > h3').text
    date = soup.select_one('#cSub > div > span > span:nth-child(2) > span').text
    body = soup.select_one('#harmonyContainer > section').get_text().strip()

url = 'https://news.v.daum.net/v/20220810005210818'
title, date, body = detail_info(url)

print(title)
print(date)
print(body)