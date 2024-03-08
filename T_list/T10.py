import requests
import pprint

# (1) vote_average가 가장 높은 영화 이름 출력하기
import requests

API_KEY = '5881d66617af20c3edea743b5472c161'
BASE_URL = 'http://api.themoviedb.org/3'
end_point1 = '/movie/popular'
payload = {
    'api_key': API_KEY,
    'language': 'ko-kr',
}

res = requests.get(BASE_URL + end_point1, params=payload)
py_res = res.json()

# 가장 높은 평점을 가진 영화 정보 추출(lambda)
popular_movie = max(py_res['results'], key=lambda x: x['vote_average'])

print("가장 높은 평점을 가진 영화의 이름:", popular_movie['title'])

# 가장 높은 평점을 가진 영화 정보 추출(for문)
highest_rating = 0
popular_movie = ''

for movie in py_res['results']:
    if movie['vote_average'] > highest_rating:
        highest_rating = movie['vote_average']
        popular_movie = movie

print("가장 높은 평점을 가진 영화의 이름:", popular_movie['title'])


# (2) 상위 가장 인기있는(vote_average) 3개의 영화의 제목 높은 순으로 출력
# 영화 정보를 vote_average를 기준으로 내림차순으로 정렬
sorted_movies = sorted(py_res['results'], key=lambda x: float(-x['vote_average']))

print("상위 가장 인기있는 3개의 영화 제목:")
for i, movie in enumerate(sorted_movies[:3], start=1):
    print(f"{i}. {movie['title']}")