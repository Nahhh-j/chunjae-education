import requests
from pprint import pprint

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2BiEaRW7xrORUYANDjKPrnvW9DAAqDJNKv3E4sm3Vwbes8db4rFSa%2FTnEVPEmaCWv1BzeVE2ek9Fv8onYt9obpQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
response = requests.get(URL)

response = response.json()
# pprint(response)

data = response.get('response').get('body').get('items')
# pprint(type(data[0]['pm25Value']))


# pprint(data)
sorted_data = sorted(data, key=lambda x : x.get('pm25Value'))


lst = [[datum.get('stationName'), datum.get('pm25Value')] for datum in sorted_data]

# 위의 코드랑 완벽히 동일!
# lst = []
# for datum in sorted_data:
#     lst.append([datum.get('stationName'), datum.get('pm25Value')])


# lst = [{datum.get('stationName') : {"pm25Value" : datum.get('pm25Value')}} for datum in sorted_data]

pprint(lst)