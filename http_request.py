
import requests
import json

import xml

resp = requests.get('http://www.baidu.com')
print(resp.text)
html = xml.dom(resp.text)
print(html)