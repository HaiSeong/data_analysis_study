# 미션4 - 크롤링

네이버 TV연예/최신뉴스/뮤직의 7월1일 ~ 7월 7일 (1주일동안)의 뉴스를 크롤링 해보기  

> ### 전략
> 지난번 코드를 그대로 사용하되 반복문을 이용해서 7일동안의 뉴스를 저장한다.

<br>

## 코드

- 기존 함수들은 그대로 사용
- datetime 패키지를 사용해서 시간 계산
- start_date와 end_date를 지정해서 그 기간의 뉴스들만 모아옴
- *날짜가 바뀌고 첫페이지에서 오류가 발생해서 우선 첫페이지에 아무것도 없으면 다시 시도하게 해놨다.*
``` python
index = 0
news_list = [] # 모든 뉴스를 담을 리스트
start_date = '2022-07-01'
end_date = '2022-07-07'
start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
date = start_date

while date <= end_date:
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
```

<br>

## 결과물
[naver_news.xlsx](https://github.com/HaiSeong/data_analysis_study/blob/main/mission4/naver_news.xlsx?raw=true)
