# https://news.naver.com/section/100
import requests as req
from bs4 import BeautifulSoup as bs
import os

# 뉴스 모든 페이지의 헤드라인 추출하기 for문 2번 적용해야 함.

# "https://news.naver.com/section/100"
# "https://news.naver.com/section/101"
# "https://news.naver.com/section/102"
# " https://news.naver.com/section/103"
# "https://news.naver.com/section/104"
# "https://news.naver.com/section/105"

for page in range(100, 106):
    url = f"https://news.naver.com/section/{page}"
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
for d in datas:
    print(d)
# print(datas)

