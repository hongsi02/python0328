#demofile.py

# 파일 쓰기
# f = open("test.txt","wt",encoding="utf-8")
# f.write("한글데이터\naaa\nbbb\n1234\n")

# f.close()
# print(f.closed)

# print("{0:,}".format(15000000))

# 파일 읽기
f = open("test.txt","rt",encoding="utf-8")

result = f.read()
print(result)
print("어디쯤", f.tell())
#처음부터 다시 리셋
f.seek(0)
print(f.readline(),end="")
print(f.readline(),end="")

#리스트로 받기
f.seek(0)
result = f.readlines()
print(result)

f.close()
