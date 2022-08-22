
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def news_croller(url): # 페이지별 크롤링 코드
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    # news_writing_time
    try:
        news_writing_time = soup.select_one('#content > div.end_ct > div > div.article_info > span:nth-child(1) > em').get_text()
    except:
        news_writing_time = ''
    # news_img
    try:
        news_img = soup.select_one('#img1')['src']
    except:
        news_img = ''
    # news_body
    try:
        news_body = soup.select_one('#articeBody').get_text().strip()
    except:
        news_body = ''
    # news_author
    try:
        news_author = soup.select_one('#content > div.end_ct > div > div.article_journalist > div > div > div > div > div > div.journalistcard_summary > div > div > div.journalistcard_summary_info > a > div.journalistcard_summary_name').get_text()
    except:
        news_author = ''

    return news_writing_time, news_img, news_body, news_author


base_url = 'https://entertain.naver.com'
browser = webdriver.Chrome('./chromedriver')
browser.get(base_url + '/now?sid=7a5#sid=7a5&date=2022-07-01&page=1')
html = browser.page_source
soup = BeautifulSoup(html, 'html')

news_list = soup.find_all('a', class_ = 'tit')
l = []
index = 0

for news in news_list:
    news_title = news.get_text()
    news_url = base_url + news['href']
    news_writing_time, news_img, news_body, news_author = news_croller(base_url + news['href'])
    l.append([index, news_title, news_url, news_writing_time, news_img, news_body, news_author])
    index+=1
    print(news_title)
    print()


df = pd.DataFrame(l, columns=['index', 'news_title', 'news_url', 'news_writing_time', 'news_img', 'news_body', 'news_author'])
df.to_excel('naver_news.xlsx', index=False)