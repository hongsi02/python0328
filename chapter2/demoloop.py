# demoloop.py

print("--파이썬의 판단근거--")
print(bool(0))
print(bool(3))
print(bool(""))
print("")

print(bool("data"))
print(bool([]))
print(bool([1,2,3]))


lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
	if i > 5:
		break
	print("Item: {0}".format(i))

print("end")

for i in lst:
	# %는 나머지 값을 구한다. ==(동일한지) !=(다른지) =(대입)
	if i % 2 == 0:
		continue
	print("Item: {0}".format(i))

print("end")

# 수열함수: range(start, end, step)
item = list(range(10))
print(item)
print(list(range(1,11)))

# 리스트 컴프리헨션(리스트 내장)
# 파이썬 개발자: 파이썬스럽다.
lst = list(range(1,11))
result = [i**2 for i in lst if i> 5]
print(result)

# 수동으로 for 루프 사용
for i in range(10):
	print(i)

# 반복문에서 필터링하는 경우
# 스칼라(단일값) 리스트(배열)
lst = [20,25,30]

# 필터링함수를 정의
def getBiggerThan20(i):
	return i>20

#iterL = filter(None,lst)
# 파이썬은 무조건 참조가 복사되어 전달 reference 이름공간의 이름을 정의 reference
#iterL = filter(getBiggerThan20,lst)
iterL = filter(lambda x:x>20, lst)
for item in iterL:
	# 서식문자로 지정: {0}, {1}, {2} 포지션을 예역해서 변경
	print("item:{0}".format(item))

for i in list(range(10)):
	print(i)
