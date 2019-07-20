from framework.Base_requests import test_requests

url = 'http://t.weather.sojson.com/api/weather/city/'
city = '101030100'
s = test_requests()
status_code, response_json, reurl= s.get(url+city)
print(status_code)
print(response_json)
print(reurl)


response = {'errno': 0, 'msg': 'success', 'result': {'id': '5b4dc7111c0ab20001c3c481', 'cname': '测试001', 'desc': '测试机器人', 'type': 0, 'settings': {'failAction': ['偶母鸡啊', '我不告诉你']}, 'lastView': '2018-07-17T18:38:09.250849551+08:00', 'nickname': '小可爱', 'age': 0, 'gender': 'male', 'hometown': '北京', 'speciality': '打游戏'}}
failAction = s.getdict(response,'failAction')
print(failAction)