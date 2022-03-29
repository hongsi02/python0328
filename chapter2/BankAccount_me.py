# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        # self.id = id
        # self.name = name 
        # self.balance = balance
        self.__id = id
        self.__name = name 
        self.__balance = balance
   
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
# 악의적으로 처리할 수 있다.
#account1.balance = 15000000
account1.__balance = 1500000 # 변경이 되지 않는다.
print(account1)
print(account1.__balance)
