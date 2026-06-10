
# incapsulation = class + data hiding + controll access
class BankAccount:
    # constructer
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #private data 
    
    # deposite method
    def deposit(self,amount):
        self.__balance += amount

    # widrowl method
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Amount is not availabel")
        else:
            self.__balance -= amount    

    # show the current balance
    def show_balance(self):
        return self.__balance
    def __str__(self):
        return f"Name={self.name}, balance={self.__balance}"
b = BankAccount("shubham",200)
b.deposit(800)
print(b.name)
print(b.show_balance())
# b.withdraw(200)
# print(b.show_balance())
# print(b)
