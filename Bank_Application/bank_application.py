
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
    
class Currency:
    def pad(self,n):
        if n<10:
            return f"0{n}"
        return f"{n}"            
    def __init__(self,rupee,paise):
        self.total=rupee*100+paise
    def __str__(self):
        sign=1
        total=self.total
        if total<0:
            sign=-1
            total=-total
        rupee=total//100
        paise=total%100
        rupee=self.pad(rupee)
        paise=self.pad(paise)
        if sign==-1:
            return f"-₹{rupee}.{paise}"    
        return f"₹{rupee}.{paise}"     

class BankAccount:
    def __init__(self, customer,account_num,rt_of_intrest,balance):
        self.customer = customer
        self.account_num = account_num
        self.rt_of_intrest = rt_of_intrest
        self.balance = balance

    def deposit(self, ammount):
         self.balance.total += ammount.total

    def withdraw(self,ammount):
       
       if self.balance.total >= ammount.total:
           self.balance.total -= ammount.total
       else:
           print("Insufficient Balance")

    
    def __str__(self):
        return  f"{self.customer}\nAccont Number: {self.account_num}\nRate of intrest: {self.rt_of_intrest}%\nBalance: {self.balance}"
    

class SavingAccount(BankAccount):
    def __init__(self, customer, account_num, rt_of_intrest, balance,account_type):
        super().__init__(customer, account_num, rt_of_intrest, balance)
        self.account_type = account_type

    def __str__(self):
        return super().__str__() + f"\nAccount Type: {self.account_type}" 

class CurrentAccount(BankAccount):
    def __init__(self, customer, account_num, rt_of_intrest, balance,overdraft_limit):
        super().__init__(customer, account_num, rt_of_intrest, balance)  
        self.overdraft_limit = overdraft_limit

    def withdraw(self, ammount):
        availabel_balance =(self.balance.total + self.overdraft_limit.total)
        if ammount.total <= availabel_balance:
            self.balance.total -= ammount.total
        else:
            print("Overdraft Limit Exceeded")     

    def __str__(self):
        return (
            super().__str__()
            + f"\nAccount Type: Current Account"
            + f"\nOverdraft Limit: {self.overdraft_limit}"
        )         



holder = AccountHolder(
    "Shubham",
    24,
    "Varanasi",
    "9022151378",
    "Cashier"
)

currency = Currency(100,15)

bank = SavingAccount(
    holder,
    "123456789",
    7,
    currency,
    "Saving Account"
)

# print(bank)

bank.withdraw(Currency(60, 25))
print(bank)