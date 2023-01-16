import pymysql
import pandas as pd


def insert_into_news(value, idx):
    index=idx
    news_title=value[1]
    news_url=value[2]
    news_writing_time = None
    if value[3] != None:
        news_writing_time=value[3].split()[0]
    news_img=value[4]
    news_body=value[5]
    news_author=value[6]
    try:
        sql = "INSERT INTO `naver`.`news`(`index`,`news_title`,`news_url`,`news_writing_time`,`news_img`,`news_body`,`news_author`) VALUES(%s,%s,%s,%s,%s,%s,%s);"
    except pymysql.err.IntegrityError:
        return


    cur.execute(sql, [index, news_title, news_url, news_writing_time, news_img, news_body, news_author])
    conn.commit()

conn = pymysql.connect(host='localhost', user='root', password='wjdgotjd99', charset='utf8mb4', db='temp') #DB 연결
cur = conn.cursor() #디폴트 커서 생성

flag = True
idx = 0;

for yyyy in range(2020, 2023):
    for mm in range(1, 13):
        df = pd.read_excel('/Users/apple/Desktop/DataStudy/mission5/news/%d_%02d_naver_news.xlsx'%(yyyy,mm))
        df = df.where((pd.notnull(df)), None)
        for i in range(len(df)):
            print(idx, df.values[i][3], df.values[i][1])
            insert_into_news(df.values[i], idx)
            idx += 1
        if yyyy == 2022 and mm == 7:
            print("완료")
            exit(0)


conn.close() #연결 닫기
