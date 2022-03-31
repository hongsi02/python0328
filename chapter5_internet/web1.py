# web1.py

from bs4 import BeautifulSoup

# 문서를 로딩(문서전체를 읽어서 문자열로 리턴): 메드 체ㄴ 호출 .read()
page = open("/Users/hongsi/Documents/Python_Work/PythonEdu/chapter5_internet/test01.html",
	"rt",encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page,"html.parser")
# 전체 문서를 보기
#print(soup.prettify())

# 문서에 있는 <p>태그를 전부 가져오기
#print(soup.find_all("p"))

# 첫번째 <p>:paragraph만 검색
#
# print(soup.find("p"))

# 조건이 있는 경우: <p class="outer-text">컨텐츠</p>
#print(soup.find_all("p",class_="outer-text")) 


#print(soup.find_all(id="first"))

# 태그 내부에 있는 문자열 출력 [0,1,2,3]
# for tag in soup.find_all("p"):
# 	print(tag.text.strip())

# 태그 내부에 있는 문자열 출력 [0,1,2,3]
for tag in soup.find_all("p"):
	content = tag.text.strip()
	content = content.replace("\n","")
	content = content.replace("\t","")
	print(content)
