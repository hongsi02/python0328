# -*- 생성자와 소멸자 -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    def __del__(self):
        print("Instance is deleted!")

my = MyClass(5)

print("전체 코드 종료")
"전체 코드 종료 후에 __del__수행됨."