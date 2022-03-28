# 불변형식과 변경형식

print("--불변형식--")
a = 1.2
print(id(a))

a= 2.3
print(id(a))

print("--가변형식--")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

def change(x):
	x[0]="H"

wordlist = ["J","A","M"]
change(wordlist)
print(wordlist)

print("--deepcopy--")
def change2(x):
	x1 =x[:] #deepcopy
	x1[0]="H"
	print(x1)


wordlist = ["J","A","M"]
change2(wordlist)
print(wordlist)

import copy
demo = {"apple":"red", "kiwi":"green"}
demo2 = copy.deepcopy(demo)
print(demo)
print(demo2)
print(id(demo))
print(id(demo2))

#print(dir())
print(globals())