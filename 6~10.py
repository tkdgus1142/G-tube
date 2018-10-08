#!C:\Python\Python37\python.exe
from bs4 import BeautifulSoup
import requests
from urllib import parse
print ("content-type:text/html; charset=euc-kr\n")
print ('''<!DOCTYPE HTML>
<!--
	Linear by TEMPLATED
    templated.co @templatedco
    Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>
	<head>
		<title>G-tube</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,300,700,500,900' rel='stylesheet' type='text/css'>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel-noscript.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-desktop.css" />
		</noscript>
	</head>
	<body>

	<!-- Header -->
		<div id="header">
			<div id="nav-wrapper">
				<!-- Nav -->
				<nav id="nav">
					<ul>
						<li><a href="index.html">Homepage</a></li>
						<li class="active"><a href="1~5.py">1 ~ 5</a></li>
						<li><a href="6~10.py">6 ~ 10</a></li>
						<li><a href="11~15.py">11 ~ 15</a></li>
						<li><a href="16~20.py">16 ~ 20</a></li>
					</ul>
				</nav>
			</div>
			<div class="container">

				<!-- Logo -->
				<div id="logo">
					<h1><a href="#">G-tube</a></h1>
					<span class="tag">By 또치와 도우너</span>
				</div>
			</div>
		</div>
	<!-- Header -->

	<!-- Main -->
		<div id="main">
			<div class="container">
				<div class="row">
					<!-- Content -->
					<div id="content" class="8u skel-cell-important">
						<section>
							<p>''')
a = []
b = []
res1 = requests.get('http://www.genie.co.kr/chart/top200')
soup1 = BeautifulSoup(res1.content, 'html.parser')
music = soup1.find_all('td', class_='info')

for i in music:
    a.append(i.find(class_='title ellipsis').get_text().strip())
for j in music:
    b.append(j.find(class_='artist ellipsis').get_text().strip())

for q in range(5, 10):
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

print('''</p>
						</section>
					</div>

				</div>
			</div>
		</div>
	<!-- /Main -->
	</body>
</html>''')
