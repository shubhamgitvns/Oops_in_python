class Person:
    def __init__(self,name,age,address,phnumber):
        self.name  = name
        self.age = age
        self.address = address
        self.phnumber = phnumber

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nPh.Number: {self.phnumber}"
    


class AccountHolder(Person):
    
    def __init__(self, name, age, address,phnumber,profession):
        super().__init__(name, age,address,phnumber)
        self.profession = profession

    def __str__(self):
        return super().__str__() + f"\nProfession: {self.profession}"

class BankAccount:
    def __init__(self, customer,account_num,rt_of_intrest,balance):
        self.customer = customer
        self.account_num = account_num
        self.rt_of_intrest = rt_of_intrest
        self.balance = balance
   
        
    
    def __str__(self):
        return  f"{self.customer}\nAccont Number: {self.account_num}\nRate of intrest: {self.rt_of_intrest}\nBalance: {self.balance}"
    
holder = AccountHolder(
    "Shubham",
    24,
    "Varanasi",
    "9022151378",
    "Cashier"
)

bank = BankAccount(
    holder,
    "123456789",
    7,
    50000
)

print(bank)