
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
import datetime

base_url = 'https://entertain.naver.com'
browser = webdriver.Chrome('./chromedriver')
index = 0

def news_croller(url): # 뉴스 기사 페이지 크롤링
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

def news_page_croller(date, page): # 뉴스 목록 페이지 크롤링
    global index # index를 global 변수로 선언

    browser.get(base_url + '/now?sid=7a5#sid=7a5' + '&date=' + date + '&page=' + str(page))
    html = browser.page_source
    soup = BeautifulSoup(html, 'html')

    news_list = soup.find_all('a', class_ = 'tit')

    if len(news_list) == 0: # 목록 페이지에서 받아온 페이지가 없으면 빈 리스트 리턴
        return []

    l = []
    for news in news_list:
        news_title = news.get_text()
        news_url = base_url + news['href']
        news_writing_time, news_img, news_body, news_author = news_croller(base_url + news['href'])
        l.append([index, news_title, news_url, news_writing_time, news_img, news_body, news_author])
        index+=1
        print(news_title, end='\n\n')

    return l


def montly_news_crolling(year, month):

    news_list = [] # 모든 뉴스를 담을 리스트
    start_date = datetime.date(year=year, month=month, day=1)

    date = start_date

    while date.month == month:
        page = 1
        str_date = str(date.strftime("%Y-%m-%d"))
        while True:
            print(str_date, "page =", page)
            temp = news_page_croller(str_date, page)
            if len(temp) == 0: # temp가 빈 리스트 일때 종료
                if page == 1: # ** 날짜가 바뀌고 첫페이지에서 오류가 발생해서 우선 첫페이지에 아무것도 없으면 다시 시도하게 해놨음
                    continue
                break
            news_list += temp
            page += 1
        date += datetime.timedelta(days=1)


    df = pd.DataFrame(news_list, columns=['index', 'news_title', 'news_url', 'news_writing_time', 'news_img', 'news_body', 'news_author'])
    df.to_excel(f'news/{year}_%02d_naver_news.xlsx'%month, index=False)


# montly_news_crolling(2022, 7) # 7월 뉴스 크롤링

for month in range(1, 7): # 2022-01 ~ 2022-06 뉴스 크롤링
    montly_news_crolling(2022, month)

for year in range(2020, 2022): # 2020-01 ~ 2021-12 뉴스 크롤링
    for month in range(1, 13):
        montly_news_crolling(year, month)