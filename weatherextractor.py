import re
import urllib.request
import urllib

#https://www.weather-forecast.com/locations/Kanpur/forecasts/latest

url1 = "https://www.weather-forecast.com/locations/"
url2 = "/forecasts/latest"
u = input("Enter City Of Your Choice: ")

url = url1 + u + url2

req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
data1 = urllib.request.urlopen( req )
m = data1.read()

m = m.decode("windows-1252")

s = m.find('<span class="phrase">')
start = int(s)+len('<span class="phrase">')
p = m.find('</span></p></td><td class="b-forecast__table-description-cell--js"')
end = int(p)
print(m[start:end])

