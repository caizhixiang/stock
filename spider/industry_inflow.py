#板块资金流入

import requests
from lxml import etree

url="http://data.eastmoney.com/bkzj/hy.html"
response = requests.get(url=url)
response.encoding="UTF-8"
print(response.text)

html = etree.HTML(response.text)
html.xpath("")
