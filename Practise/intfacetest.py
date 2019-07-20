# -*- coding: UTF-8 -*-

import requests
import re

test_url = 'https://github.com/login'
s = requests.session()
r = s.get(test_url)
rewuit = r.text
tokens = re.findall(r'<input type="hidden" name="authenticity_token" value="(.*?)" />', rewuit)
token = tokens[0]
print(token)
url ='https://github.com/session'
payload= {'commit': 'Sign in',
           'utf8': '✓',
           'authenticity_token':token,
           'login':'maomaokeen',
           'password':'GITmaomao0125'}
r1 = s.post(url, data=payload)
print(r1.status_code)
print(r1.text)
print(r1.cookies)