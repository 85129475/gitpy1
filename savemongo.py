import requests
import time
import pymongo



client=pymongo.MongoClient('118.24.91.182',27017)

book_weather=client['weather']
sheet_weather=book_weather['sheet_weather_3']
url='https://cdn.heweather.com/china-city-list.txt'
strhtml=requests.get(url)
data=strhtml.text
data1=data.split('\n')
for i in range(6):
    data1.remove(data1[0])
for item in data1:

    url = 'https://free-api.heweather.net/s6/weather/forecast?location=' + item[2:14] + \
          '&key=bc02c9317ea040a3bc794de1f889a822'
    strhtml = requests.get(url)
    time.sleep(1)
    dic =strhtml.json()
    sheet_weather.insert_one(dic)