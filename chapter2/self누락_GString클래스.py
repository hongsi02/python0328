# 전역변수
str = "Not Class Member"
class GString:
    # 클래스 멤버 변수 (static 키워드 없이 위치를 가지고 구분)
    # 주로 데이터를 공유
    num_person = 0
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
        GString.num_person +=1
    def set(self, msg):
        self.str = msg
    def print(self):
        print(str)
        print("my name is {0}".format(GString.num_person))

g = GString()
g.set("First Message")
g.print()
