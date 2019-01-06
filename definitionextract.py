import re
import urllib.request
import urllib

#https://www.weather-forecast.com/locations/Kanpur/forecasts/latest

url1 = "https://dictionary.cambridge.org/dictionary/english/"
u = input("Enter Word: ")

url = url1 + u

req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
data1 = urllib.request.urlopen( req )
m = data1.read()

m = m.decode("utf-8")

s = m.find('property="og:description"')
start = int(s)+len('property="og:description"') + len('content=""')
p = m.find('<meta property="og:image" ') - len('&helli&hellip;. Learn more." />')
end = int(p)
print(m[start:end])

