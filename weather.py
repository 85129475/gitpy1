import requests
import time,datetime


url='https://cdn.heweather.com/china-city-list.txt'
strhtml=requests.get(url)
data=strhtml.text
data1=data.split('\n')
for i in range(6):
    data1.remove(data1[0])
for item in data1:


    #print(item[2:14])
    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + item[2:14] + \
          '&key=bc02c9317ea040a3bc794de1f889a822'
    strhtml = requests.get(url)
    time.sleep(1)
    #print(strhtml.text)
    dic =strhtml.json()
    for item in dic['HeWeather6'][0]['daily_forecast']:
        print(item['tmp_max'])