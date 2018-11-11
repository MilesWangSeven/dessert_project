from urllib.request import quote
import requests
import bs4
import webbrowser
import pyperclip
import time
import re
import base64

'''
原理:
迅雷下载地址："thunder://"+Base64编码("AA"+"真实地址"+"ZZ")
QQ旋风下载地址:"qqdl://"+Base64编码("真实地址")
'''

THUNDER_HEADER = "thunder://"
THUNDER_PREFIX = "AA"
THUNDER_SUFFIX = "ZZ"
QQ_HEADER = "qqdl://"
ERROR = "传入的URL有误，请检查！"


# 判断url是否有效
def checkUrl(func):
    def wrapper(url):
        if re.match(r"(http|https|ftp|ed2k|thunder|qqdl)://", url):
            return func(url)
        else:
            return ERROR
    return wrapper


@checkUrl
def real2QQ(url):
    url = base64.b64encode(url.encode("utf-8"))
    url = QQ_HEADER + url.decode("utf-8")
    return url


@checkUrl
def qq2Real(url):
    url = url[len(QQ_HEADER):]
    url = base64.b64decode(url.encode("utf-8"))
    url = url.decode("utf-8")
    return url


@checkUrl
def real2Thunder(url):
    url = THUNDER_PREFIX + url + THUNDER_SUFFIX
    url = base64.b64encode(url.encode("utf-8"))
    url = THUNDER_HEADER + url.decode("utf-8")
    return url


@checkUrl
def thunder2Real(url):
    url = url[len(THUNDER_HEADER):]
    url = base64.b64decode(url.encode("utf-8"))
    url = url.decode("utf-8")
    url = url[len(THUNDER_PREFIX):-len(THUNDER_SUFFIX)]
    return url


@checkUrl
def qq2Thunder(url):
    return real2Thunder(qq2Real(url))


@checkUrl
def thunder2QQ(url):
    return real2QQ(thunder2Real(url))


headers = {'User-Agent':
               r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
while True:
    name_movie = pyperclip.paste()
    rec = input('请确认搜索《{}》,直接回车搜索或者输入电影名。'.format(name_movie))
    if not rec and name_movie:
        break
    if rec:
        name_movie = rec
        break
    time.sleep(0.2)
print('搜索{}中...'.format(name_movie))
gbk_movie = name_movie.encode('gbk')
url_movie = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword={}'.format(quote(gbk_movie))
res = requests.get(url_movie, headers=headers)
print('搜到电影链接网页。')
print(url_movie)

bs_movie = bs4.BeautifulSoup(res.text, 'html.parser')
link = bs_movie.select('.co_content8 b a')
if r'/html/' not in link[0].get('href'):
    print('未搜到电影下载网页')
    input('按回车退出程序')
    exit(0)
final_link = 'http://www.ygdy8.com{}'.format(link[0].get('href'))
print(final_link)
res_text = requests.get(final_link, headers).content.decode('gbk')
print('搜到电影下载网页。')
print(final_link)

bs_download = bs4.BeautifulSoup(res_text, 'html5lib')
# final_download = bs_download.select('table tbody tr a')
final_download = bs_download.select('a')
# final_download = bs_download.find_all('a', href="WORD-WRAP: break-word")
# final_download = bs_download.find_all(text=re.compile("ftp://*"))
# final_download = re.findall(r'"thunder://(.*?)"', res_text, re.S | re.M)
# final_download = re.findall(r'"ftp://(.*?)"', res_text, re.S | re.M)
# with open('html.txt', 'w') as f:
#     f.write(res_text)

real_download = ''
for download in final_download:
    download = download.get('href')
    # print(download)
    if 'ftp:' in download:
        real_download = real2Thunder(download)
    elif 'magnet:' in download:
        real_download = download
        break

if real_download:
    webbrowser.open(real_download)
    print('搜到电影下载链接')
    print(real_download)
else:
    print('未找到下载链接')
input('按回车退出程序')