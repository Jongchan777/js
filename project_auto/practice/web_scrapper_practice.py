#5.1 Introduction
# HTML tag에 대한 기본 용법을 알아야 함

#5.2 Installation
# 1. 어떤 웹사이트인지에 따라서 웹 스크래핑이 가능한 / 불가능한으로 나뉨
# 2. 어떤 우베사이트는 데이터 스크래핑해가는걸 극도로 싫어해서 이용약관에 써놓기도 함
# beautifulsoup4 설치

#5.3 Initial Request
# requests library를 이용하여 접근하는 page에 HTML code를 불러오기
#5.4 BeautifulSoup
from requests import get
from bs4 import BeautifulSoup

"""
base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser") # html을 몽땅 Text로 받아오고, 해당 html을 beautifulSoup를 이용하기위해 soup라는 변수에 넣어줌
  # print(soup.find_all('title')) html 태그가 title인 녀석을 찾아서 콘솔에 프린트
  jobs = print(soup.find_all('section', class_="jobs")) # jobs라는 변수에 html 태그가 섹션인 녀석 중, 클래스명이 jobs인 녀석을 몽땅 불러와서 넣기
  print(jobs)
"""


#5.5 Keyword Arguments
# positioning이란, 이미 정해진 위치라면 고려하지 않아도(생략해도) 됨
# 위치를 고려하고싶지 않다면, argument를 명시해주면 됨
# jobs = print(soup.find_all('section', class_="jobs")) 해당 argument에 class_를 사용할 수 있는건 find_all이 엄청나게 많은 argument를 가지고 있기 때문임
# class를 argument로 사용하지 못하는 이유는, 이미 python에 존재하기 때문에 사용 불가

def say_hello(name, age):
  print(f"안녕? 내 이름은 {name}이고, 내 나이는{age}야 만나서 반가워")

say_hello("종찬", 31)
say_hello(age=31, name="종찬")

#5.6 Job Posts
# 각 항목에 있는 section_ul_li를 뽑아내고 싶음
"""
base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{base_url}{search_term}")


soup = BeautifulSoup(response.text, "html.parser") # html을 몽땅 Text로 받아오고, 해당 html을 beautifulSoup를 이용하기위해 soup라는 변수에 넣어줌
jobs = soup.find_all('section', class_="jobs") # jobs라는 변수에 html 태그가 섹션인 녀석 중, 클래스명이 jobs인 녀석을 몽땅 불러와서 넣기
for job in jobs:
  posts = job.find_all('li')
  posts.pop(-1)
  for post in posts:
    print(post)
    print("//////////////////////////////////////////////////////////////////////////")
"""
#5.7 Job Extraction
base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{base_url}{search_term}")


soup = BeautifulSoup(response.text, "html.parser") # html을 몽땅 Text로 받아오고, 해당 html을 beautifulSoup를 이용하기위해 soup라는 변수에 넣어줌
jobs = soup.find_all('section', class_="jobs") # jobs라는 변수에 html 태그가 섹션인 녀석 중, 클래스명이 jobs인 녀석을 몽땅 불러와서 넣기
for job in jobs:
  posts = job.find_all('li')
  posts.pop(-1)
  for post in posts:
    anchors = post.find_all('a')
    anchor = anchors[1]
    link = anchor['href']
    company, kind, region = anchor.find_all("span", class_="company")
    title = anchor.find("span", class_="title")
    print(company, kind, region, title)
    print("//////////////////////////////////////////////////////////////////////////")
    print("//////////////////////////////////////////////////////////////////////////")

#5.8 Saving Results
# span에서 텍스트 추출하기 그리고 저장