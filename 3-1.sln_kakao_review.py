from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#### 1. 웹드라이버 및 객체생성, 페이지 요청
# 크롬 브라우저 옵션
options = webdriver.ChromeOptions() # 크롬 브라우저 옵션 객체 생성
# 서버에서는 창을 안띄운다. -> 창을 띄워야하면 서버에서 오류가 나기 때문에 서버에 배포할 때 살린다.
# options.add_argument('headless') # 브라우저 안띄우기

options.add_argument('lang=ko_KR') # KR 언어
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# ChromeDriver 경로를 지정하는 Service 객체 생성

# 실행할 때마다 현재 크롬브라우저와 동일한 버전의 드라이버 다운로드함
# driver = webdriver.Chrome(ChromeDriverManager().install())
chrome = webdriver.Chrome(options=options)

# driver를 통해 url의 요청을 보냄
url = "https://map.kakao.com/"
chrome.get(url)

title = chrome.title # 브라우저의 태그이다.
print(title)
time.sleep(2) # cpu 5sec간 제어를 멈춤 # 무조건 멈춤
# driver.implicitly_wait(5) # 뒤에 있는 명령이 실행되도록 최대 5sec 기다려주는 것 실행되면 바로 넘어감 

# 검색 키워드
place = '스타벅스'

#### 2. 카카오 맵에서 자동 검색 기능
# 1) 검색어 입력
search_area = chrome.find_element(By.XPATH, '//*[@id="search.keyword.query"]') # 태그, 아이드, 클래스... 어떤 걸로 XPASS로 하려면 By가 필요함
search_area.send_keys(place) # 검색어 입력
time.sleep(1)

# 2) 엔터키 입력(키인)
# //*[@id="search.keyword.submit"]
chrome.find_element(By.XPATH, '//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
time.sleep(3)
# 키보드를 객체로 파악하고 키 값을 넣어준다.



# 3) BS로 정보를 파싱해서 데이터 추출
# 현재 브라우저의 html 코드(DOM 트리)를 html변수에 저장
html = chrome.page_source

soup = BeautifulSoup(html, 'html.parser')
time.sleep(1)
print(soup)

# - 터미널에서 출력하는 내용을 파일에 저장하고 싶을 때 사용
#sys.stdout = open('kakaomap3.txt', 'w')
#print(cafe_lists)
# sys.stdout.close() 
# 장소의 li 목록
# ul.placelist > li.PlaceItem
caffee_list = soup.select('ul.placelist > li.PlaceItem.clickArea')
time.sleep(1)
print(len(caffee_list))

# 매장별 리뷰 저장
# {
# "매장1" : ["리뷰1", "리뷰2", ,............]
# "매장2" : ["리뷰1", "리뷰2", ,............]
# "매장3" : ["리뷰1", "리뷰2", ,............]
# }
# place_reviews["매장별1"] = ["리뷰1", "리뷰2"...........]
place_reviews = {}
for i, cafe in enumerate(caffee_list):
    # print(i, cafe)
    # print("-"*50)
    place_name = cafe.select_one(".head_item  .link_name").text
    print(place_name)

    # 리뷰 수집 -> 상세보기 클릭
#    //*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]
#    //*[@id="info.search.place.list"]/li[2]/div[5]/div[4]/a[1]
#    //*[@id="info.search.place.list"]/li[3]/div[5]/div[4]/a[1]
#    //*[@id="info.search.place.list"]/li[4]/div[5]/div[4]/a[1]
#    //*[@id="info.search.place.list"]/li[5]/div[5]/div[4]/a[1]
    x_path = f'//*[@id="info.search.place.list"]/li[{i+1}]/div[5]/div[4]/a[1]'
    chrome.find_element(By.XPATH, x_path).send_keys(Keys.ENTER)
    time.sleep(2)
    chrome.switch_to.window(chrome.window_handles[-1]) # 열려있는 마지막 탭
    time.sleep(2)
    chrome.close()
    chrome.switch_to.window(chrome.window_handles[0]) # 열려있는 처음 탭
# chrome.switch_to.window(chrome.window_handles[0]) -> 창이동, 0번 검색창으로 다시 이동
time.sleep(2)
# 열려있는 창을 닫는다.
chrome.close()
# 윈도우를 종료한다.
chrome.quit()