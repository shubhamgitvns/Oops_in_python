class Time:
    def __init__(self,hour,min):
        self.hour = hour
        self.min = min

    def differnece(self,other):
        total1 = self.hour *60 + self.min
        total2 = other.hour * 60 + other.min

        diff = abs(total1-total2)
        # hours = diff // 60
        # mins = diff % 60
        return f"{diff} Minutes" 

            

    def __str__(self):

        
        if self.hour > 23 or self.hour < 0:
            return "Enter Valid Time"

        if self.min > 59 or self.min < 0:
            return "Enter Valid Time"

        if self.hour == 0:
            return f"12:{self.min} AM" 
        
        if self.hour == 12:
            return f"12:{self.min} PM"
        
        if self.hour >= 12:
            hour = self.hour % 12 
            return (f"{hour}:{self.min} PM")   
        else:
            return (f"{self.hour}:{self.min} AM")  





t1 = Time(10,2)
t2 = Time(17,5)
print(t1)
print(t2)
print(t1.differnece(t2))