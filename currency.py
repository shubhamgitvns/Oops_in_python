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
    def __add__(self,other):
        return Currency(0,self.total+other.total)
    
    def __sub__(self, other):
        return Currency(0,self.total-other.total)
c1=Currency(10,0)                          
print(c1)
print(c1+c1)
print(c1-c1)