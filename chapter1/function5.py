# function5.py

def union(*ar):
	#지역변수를 리트로 초기화
	result = []
	for item in ar:
		for x in item:
			if x not in result:
				result.append(x)
	
	return result

# 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다 함수(이름이 없다!)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))

print(globals())



