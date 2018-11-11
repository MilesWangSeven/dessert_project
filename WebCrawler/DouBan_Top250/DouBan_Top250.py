import requests
import bs4
import json
import time

url_str = 'https://movie.douban.com/top250?start={}&filter='
movie_list = ['movie,score']

for i in range(0, 250, 25):
    url = url_str.format(i)
    print(url)
    res = requests.get(url)
    bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
    bs_ol = bs_res.find('ol', attrs={'class': 'grid_view'})
    bs_li = bs_ol.find_all('li')
    for li in bs_li:
        movie_name = li.find('span', attrs={'class': 'title'})
        movie_score = li.find('span', attrs={'class': 'rating_num'})
        movie_list.append('{},{}'.format(movie_name.text, movie_score.text))
    print(movie_list[-25:])
    time.sleep(1)

with open('Douban_MovieTop20.csv', 'w') as f:
    f.write('\n'.join(movie_list))
