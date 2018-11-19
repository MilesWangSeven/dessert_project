import requests
import json

res = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
json_res = json.loads(res.text)
print('请输入你选择的词库编号，按Enter确认')
for index, item in enumerate(json_res['data']):
    print('{:>02d}. {}'.format(index+1, item[1]))
try:
    index = int(input('-->')) - 1
    category = json_res['data'][index][0]
except:
    print('Sorry,please input a number above and try it again.')
    exit(0)
print(category)