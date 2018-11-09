from urllib.request import quote
import requests
import bs4
import webbrowser
import pyperclip
import time

while True:
    name_movie = pyperclip.paste()
    if name_movie:
        break
    time.sleep(0.2)
print('搜索{}中...'.format(name_movie))
gbk_movie = name_movie.encode('gbk')
url_movie = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword={}'.format(quote(gbk_movie))
res = requests.get(url_movie)
bs_movie = bs4.BeautifulSoup(res.text, 'html.parser')
link = bs_movie.select('.co_content8 b a')
final_link = 'http://www.ygdy8.com{}'.format(link[0].get('href'))
res_text = requests.get(final_link).text
bs_download = bs4.BeautifulSoup(res_text, 'html.parser')
# final_download = bs_download.select('table tbody tr a')
final_download = bs_download.findAll('td', style="WORD-WRAP: break-word")
for download in final_download:
    print(download.a.get('href'))
# webbrowser.open(final_download[-1].a.get('href'))
