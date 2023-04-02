# 爬虫爬取百度搜索粮食的结果页面，偶尔好用偶尔不好用。也是奇葩了
# 原帖http://www.51testing.com/html/61/n-4476161.html

import json

import requests
from lxml import etree

# 模拟请求头，发起requests请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
respones = requests.post("https://baidu.com/s?wd=奶子&lm=1", headers=headers)
# 对获取到的源码整理分析，通过xpath定位资源
r = respones.text
html = etree.HTML(r, etree.HTMLParser())
r1 = html.xpath('//h3')
r2 = html.xpath('//*[@class="c-abstract"]')
r3 = html.xpath('//*[@class="t"]/a/@href')

# 把爬取到的资源循环读取保存
for i in range(10):
    # try:
    r11 = r1[i].xpath('string(.)')
    r22 = r2[i].xpath('string(.)')
    r33 = r3[i]
    with open('ok.txt', 'a', encoding='utf-8') as c:
        c.write(json.dumps(r11, ensure_ascii=False) + '\n')
        c.write(json.dumps(r22, ensure_ascii=False) + '\n')
        c.write(json.dumps(r33, ensure_ascii=False) + '\n')
    print(r11, end='\n')
    print('————————————————————')
    print(r22, end='\n')
    print(r33)
# except IndexError:
#     pass
