import requests as re
from bs4 import BeautifulSoup as bs

url = "https://klavogonki.ru/vocs/559/"

src = re.get(url).text
bs1 = bs(src,"lxml")
f = bs1.find_all("td",class_ ="text")
f2 = [str(x.text) for x in f]
print(f2)
