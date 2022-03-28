# function2.py
# 함수 내부의 이름을 해석하는 규칙 (LGB)

x = 2  
a =3
#
def func(a):
	return a+x

print(func(1))

def func2(a):
	x = 5
	return a+x

print(func2(1))

def func3():
	return a+x

print(func3())

#기본값이 있는 경우
def times(a=10,b=20):
	return a*b

print(times())
print(times(5))
print(times(5,6))
print(times(b=4))


# 키워드 인자(파라메터명을 명시)
def connectURI(server, port):
	strURL="http://" + server + ":" + port
	return strURL

print(connectURI("credu.com","80"))
print(connectURI(port="80",server="credu.com"))

