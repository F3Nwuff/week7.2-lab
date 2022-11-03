class account:
    def __init__(self,balance):
        self.__balance = balance
    def getbal(self):
        print(self.__balance)
        return True
    def deposit(self,balance):
        self.__balance += balance
        return True
    def pay(self,balance):
        if self.__balance >= balance:
            self.__balance -= balance
            return True
        else:
            return False
class User:
    def __init__(self,username,acc):
        self.__username = username
        self.__acc = account(acc)
    def getbal(self):
        return self.__acc.getbal()
    def deposit(self, i):
        return self.__acc.deposit(i)
    def pay(self, j):
        return self.__acc.pay(j)