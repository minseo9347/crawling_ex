# https://news.naver.com/section/100
import requests as req
from bs4 import BeautifulSoup as bs
import os
import csv

# html 문서요청

# print(type(html))

# soup 객체 생성

# print(soup)
# print(type(soup))
# news head line을 싸고 있는 li요소의 selector 
# #_SECTION_HEADLINE_LIST_gub5x > li:nth-child(1)

# SECTION_HEADLINE_LIST_gub5x

# 셀렉터가 저장한 첫본째 요소를 가져옴
# datas = soup.select_one(".sa_list li.sa_item")

# 클래스 일 때에는 앞에 . 아이디 일 때는 앞에 #이다.
# 셀렉터가 지정한 모든 요소 추출
# html 문서요청

# print(datas)
# https://news.naver.com/section/100
import requests as req
from bs4 import BeautifulSoup as bs
import os
import csv
url = "https://news.naver.com/section/100"
# html 문서요청
html = req.get(url).text
# print(type(html))

# soup 객체 생성
soup = bs(html, 'html.parser')
# print(soup)
# print(type(soup))
# news head line을 싸고 있는 li요소의 selector 
# #_SECTION_HEADLINE_LIST_gub5x > li:nth-child(1)

# SECTION_HEADLINE_LIST_gub5x

# 셀렉터가 저장한 첫본째 요소를 가져옴
# datas = soup.select_one(".sa_list li.sa_item")

# 클래스 일 때에는 앞에 . 아이디 일 때는 앞에 #이다.
# 셀렉터가 지정한 모든 요소 추출
datas = soup.select(".sa_list li.sa_item")
# print(datas)
with open('news.data.csv', "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["섹션", "헤드라인", "이미지 URL"])
    for data in datas:
        # print(data.select_one('.sa_text_strong').get_text())
        head_line = data.select_one('.sa_text_strong').get_text()
        img_tag= data.select_one('img[data-src]')
        # print(img_tag)

        if img_tag:
            img_src_value = img_tag['data-src']
            print(img_src_value.split('?')[0])


            writer.writerow([head_line, img_src_value])
            print(f"✅ 저장 완료: {head_line} | {img_src_value}")    
        else:
            print("data=src 속성을 가진 img 태그를 찾을 수 없습니다.")
        print(f"{head_line}, {img_tag}")
        

# https://news.naver.com/section/100

#import requests as req
#from bs4 import BeautifulSoup as BS
#import os

#url = "https://news.naver.com/section/100"

# html 문서 요청
#html = req.get(url).text
# print(type(html))

# soup 객체 생성
#soup = BS(html, 'html.parser')
# print(soup)