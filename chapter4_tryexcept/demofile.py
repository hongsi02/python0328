#demofile.py
f = open("test.txt","wt",encoding="utf-8")
f.write("aaa\nbbb")

f.close()
print(f.closed)

print("{0:,}".format(15000000))