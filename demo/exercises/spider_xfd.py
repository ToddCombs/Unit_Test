# 抓取新发地菜价
# http://www.51testing.com/html/61/n-4479861.html

import pandas as pd
import requests
from tqdm import tqdm

headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

dfList = []
url = r'http://www.xinfadi.com.cn/getPriceData.html'  # 新发地菜价详情地址

for page in tqdm(range(1, 5373)):
    FormData = {
        "limit": 20,
        "current": page,
        "pubDateStartTime": "2021/01/01",
        "pubDateEndTime": "2021/12/01",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""
    }

    r = requests.post(url, data=FormData, headers=headers)
    data = r.json()
    dataList = data['list']
    df = pd.DataFrame(dataList)
    dfList.append(df)

df = pd.concat(dfList)
df.to_excel(r'菜价历史价格行情.xlsx', index=None)
