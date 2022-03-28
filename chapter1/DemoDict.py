# DemoDict.py

from turtle import color


def calc(a,b):
	return a+b, a*b

result = calc(3,4)
print(result)

print(result[0])
print(result[1])

# 하나로 모아서 입력

args=(5,6)
print(calc(*args))

# 타입캐스팅 (형식 변환):List, Tuple, Set 형식 변환
a = set((1,2,3))
print(a)
b= list(a)
print(b)
b.append(5)
print(b)

# 딕셔너리 (JSON:  Java script의 객체 표시)
color={"apple":"red","banana":"yellow","cherry":"red"} 
print(color)
print(len(color))
print(color["apple"])

device = {"아이폰":5,"아이패드":10,"윈도우 타블렛":20}
print(device)
device["맥프레"]=15
device["아이폰"] = 6
print(device)
del device["아이폰"]
print(device)

#참조
mydevice = device

mydevice["에어팟"]=10 

# id : 주소와 비슷한 값을 가리킴
print(id(device))
print(id(mydevice))

print(device)
print(mydevice)
# phone = {"kim":"1111","lee":"2222","park":"3333"}
# print(phone.keys())