class Time:
    def __init__(self,hour,min):
        self.hour = hour
        self.min = min

        
            

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





t = Time(12,2)
print(t)