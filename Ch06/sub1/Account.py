class Account:
     

    def __init__(self, bank, id, name, balance):
        self.__bank = bank
        self.__id = id
        self.__name = name
        self.___balance = balance

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        self.__balance -= money

def show(self):
        print('은행명 :', self._bank)
        print('계좌번호 :', self._id)
        print('입금주 :', self._name)
        print('현재잔액 :', self._balance)