#coding:utf8
import requests

def getWeather(city):
    r = requests.get(url=u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    return '%s:%s , %s' % (city,data['low'],data['high'])

print(getWeather(u'北京'))
print(getWeather(u'长春'))
