# classtest.py

# 클래스 새로운 type 정의
class Person:
	# 초기화(생성자 메서드)
	def __init__(self):
		self.name = "default name"
	def print(self):
		print("My name is {}".format(self.name))

# 인스턴스 생성
p1 = Person()
p2 = Person()
p2.name = "전우치"
p1.print()
p2.print()

Person.title="New title"
print(p1.title)
print(p2.title)
print(Person.title)

str = "Not Class Memeber"

'''
컴파일러 : C, C++, C#, VB

소스코드 ----> 기계어 코드(실행파일이 나옴 *.exe, *.app...)
     (빌드, 만들기, 컴파일)

번역을 하면 통으로 보는 작업(정적 타입)

인터프리터(스크립트): python, R, JavaScript
라인단위로 해석

통역을 하는 느낌(다이나믹하게 확장)

'''