import re
import urllib.request
import urllib

url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")
url = url + stock

req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
data1 = urllib.request.urlopen( req )
m = data1.read()

m = m.decode("windows-1252")



s = m.find('US$')
start = int(s)
end = start+10
print(m[start:end])


s = re.search('US$',m)
print(s)
