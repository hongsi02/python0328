# web2.py
# 웹서버와 통신할 경우 사용
import urllib.request
# 코롤링에 사용
from bs4 import BeautifulSoup


# 파일로 저장
f = open("./chapter5_internet/webtoon.txt","wt",encoding="utf-8")
# 페이징 처리(1페이지가 10개 * 5개)
for i in range(1,6):
	url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
	print(url)
	data = urllib.request.urlopen(url)
	soup = BeautifulSoup(data,"html.parser")

	cartoons = soup.find_all("td", class_="title")
	print("개수:{0}".format(len(cartoons)))
	title = cartoons[0].find("a").text 
	link = cartoons[0].find("a")["href"]
	print(title)
	print(link)
	
	for item in cartoons:
		title = item.find("a").text
		print(title)
		print(link)
		f.write(title+"\n")
		f.write(link+"\n")

f.close()

print("크롤링 종료")




