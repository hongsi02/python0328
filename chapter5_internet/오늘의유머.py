# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("./today.txt", "wt", encoding="utf-8")
# 페이징 처리를 0에서 9번까지
for n in range(0,10):

	#클리앙의 중고장터 주소 
	#data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
	data = 'http://www.todayhumor.co.kr/board/list.php?kind=total&table=total&page=3' + str(n)
	#print(data)
	#웹브라우져 헤더 추가 
	req = urllib.request.Request(data, \
								headers = hdr)
	data = urllib.request.urlopen(req).read()
	# 한글이 깨지는 경우 디코딩이 필요
	page = data.decode('utf-8', 'ignore')
	soup = BeautifulSoup(page, 'html.parser')

    # <span class="subject_fixed" data-role="list-title-text" title="사용감 거의없는 서피스프로5 풀셋">
	# 			사용감 거의없는 서피스프로5 풀셋
	# </span>
	list = soup.find_all('td', attrs={'class':'subject'})
	#list = soup.findAll('a', attrs={'class':'list_subject'})

	for item in list:
			try:
				tag = item.find("a")
				title = tag.text
				print(title.strip())
				f.write(title.strip() + "\n")
				#<a class='list_subject'><span>text</span><span>text</span>
				# span = item.contents[1]
				# span2 = span.nextSibling.nextSibling
				# title = span2.text 
				# if (re.search('맥북', title)):
				# 		#pass
				# 		print(title.strip())
				# 		print("she")
				# 		print('https://www.clien.net'  + item['href'])
				# 		print("me")
				# 		f.write(title.strip() + "\n")
			except:
					pass
        
f.close()
print("크롤링 종료")
