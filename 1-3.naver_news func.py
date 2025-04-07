import requests as req
from bs4 import BeautifulSoup as bs
import csv

def get_news_from_section(section: int):

    url = f"https://news.naver.com/section/{section}"
    response = req.get(url)

    soup = bs(response.text, 'html.parser')
    datas = soup.select(".sa_list li.sa_item")

    news_list = []
    with open('news.data.csv', "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["헤드라인", "이미지 URL"])
        for data in datas:
            # 헤드라인 추출
            headline_tag = data.select_one('.sa_text_strong')
            headline = headline_tag.get_text()

            # 이미지 URL 추출
            img_tag = data.select_one('img[data-src]')
            img_url = img_tag['data-src'].split('?')[0]
            # 리스트에 저장
            news_list.append((headline, img_url))
            # CSV에 저장
            writer.writerow([headline, img_url])

        return news_list
    get_news_from_section(section: 101)