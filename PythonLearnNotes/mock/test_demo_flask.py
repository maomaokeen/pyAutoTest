import requests

test_url='http://localhost:7001/test'
data={'user_id': '1aaa'}
#a=requests.post(test_url)
#ra=a.json()
#b=requests.get(test_url, data=data)
#rb=b.json()
c=requests.post(test_url, data=data)
rc=c.json()

#print(ra)
#print(rb)
print(rc)