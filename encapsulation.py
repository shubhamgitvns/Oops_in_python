
# incapsulation = class + datahiding + controll access
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount    

    def show_balance(self):
        return self.__balance

b = Bank("shubham",200)
b.deposite(500)
print(b.name)
print(b.show_balance())