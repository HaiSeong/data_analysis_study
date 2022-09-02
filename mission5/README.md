# 미션5 - 크롤링

네이버 TV연예/최신뉴스/뮤직의 달별 뉴스 크롤링 해보기 -> 반복문으로 원하는 년도, 월의 뉴스 크롤링 하기

> ### 전략
> mission4의 코드를 변형해 함수화 하고 반복문을 이용해 기간별로 뉴스를 크롤링 한다.

<br>

## 코드

- while date.month == month -> day를 하나씩 증가시키다가 지정한 month가 아니면 정지한다.
- 연도와 달을 엑셀파일으 이름으로 해서 news 디렉토리에 저장했다.
``` python
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


montly_news_crolling(2022, 7) # 7월 뉴스 크롤링

for month in range(1, 7): # 2022-01 ~ 2022-06 뉴스 크롤링
    montly_news_crolling(2022, month)

for year in range(2020, 2022): # 2020-01 ~ 2021-12 뉴스 크롤링
    for month in range(1, 13):
        montly_news_crolling(year, month)
```

<br>

## 결과물
[2022_07_naver_news.xlsx](https://github.com/HaiSeong/data_analysis_study/blob/main/mission5/news/2022_07_naver_news.xlsx?raw=true)
