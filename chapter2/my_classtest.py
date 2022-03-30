# classtest.py
class Person:
	Name = "Default Name"
	def Print(self):
		print("My name is {0}".format(self.Name))

p1 = Person()
p1.Print()

p1.Name = "홍성일"

# 바운드 메서드 호출
p1.Print()
# 언바운드 메서드 호출
Person.Print(p1)

# 동적으로 멤버변수 추가할 수 있음
# 이렇게 되어도 되는 건가??
p1.age = 20
print("p1's age:",p1.age)
# Not defined
# print("p2's age is:",p2.age)
