import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

rank = 1
for w in range(5):
    data = requests.get(
        'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg='+str(w), headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    movies = soup.select(
        '#body-content > div.newest-list > div > table > tbody > tr')

# for page in range(3):
#     raw = requests.get('https://search.naver.com/search.naver?&where=news&query=아시안게임&start=' + str(i * 10 + 1), headers={'User-Agent': 'Mozilla/5.0'}).text

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦

# select를 이용해서, tr들을 불러오기


# movies (tr들) 의 반복문을 돌리기
    for movie in movies:
        # movie 안에 a 가 있으면,
        a_tag = movie.select_one('td.info > a.title.ellipsis')

        star = movie.select_one('td.info > a.artist.ellipsis')
        star = star.text
    # img 태그의 alt 속성값을 가져오기
        title = a_tag.text                                  # a 태그 사이의 텍스트를 가져오기
    # td 태그 사이의 텍스트를 가져오기
        
        doc = {
            'rank' : rank,
            'title' : title,
            'artist' : star
        }
        db.songs.insert_one(doc)

        print(rank, title.strip(), '/', star.strip())
        rank += 1

