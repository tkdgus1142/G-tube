#!C:\Python\Python37\python.exe
from bs4 import BeautifulSoup
import requests
from urllib import parse
print ("content-type:text/html; charset=euc-kr\n")
print ('''<!doctype html>
<html>
<head>
  <title>G-tube</title>
  <meta charset="utf-8">
</head>
<body>
<h1><a href="index.html">Gtube</a></h1>
<ol>
<li><a href="1.html">HTML</a></li>
<li><a href="2.html">CSS</a></li>
<li><a href="3.html">JavaScript</a></li>
</ol>''')
a = []
b = []
res1 = requests.get('http://www.genie.co.kr/chart/top200')
soup1 = BeautifulSoup(res1.content, 'html.parser')
music = soup1.find_all('td', class_='info')

for i in music:
    a.append(i.find(class_='title ellipsis').get_text().strip())
for j in music:
    b.append(j.find(class_='artist ellipsis').get_text().strip())

for q in range(0, 5):
    res2 = requests.get('https://www.youtube.com/results?search_query='+parse.quote(b[q])+'+'+parse.quote(a[q]))
    soup2 = BeautifulSoup(res2.content, 'html.parser')
    lis = soup2.find('a', attrs={'class': 'yt-uix-tile-link', 'data-sessionlink': True})
    title = lis.get_text()
    video_link = 'https://www.youtube.com/embed' + lis['href']
    video = video_link.replace('watch?v=', '')
    print('''<li>''')
    print (q+1)
    print (title)
    print ('''<p><iframe width="560" height="315" src="''')
    print (video)
    print ('''" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></li>''')

print ('''</body></html>''')
