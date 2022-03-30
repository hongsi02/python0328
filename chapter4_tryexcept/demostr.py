# demostr.py
# str은 기본적으로 파이썬 메모리에 올라온다.
print(dir(str))

strA = " << spam and ham >>> "
print(strA)
print(strA.strip("<> "))

result = strA.strip("<> ")
print(result)

strB = "python is powerful"
print(len(strB))
print(strB.capitalize())
print(strB.count("p",7))
print(strB.endswith("ful"))

lst = result.split()
print(lst)

