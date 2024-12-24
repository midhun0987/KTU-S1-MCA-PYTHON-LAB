#4.Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time.

#Date:5-12-24

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __add__(self, other):
        second = self.second + other.second
        minute = self.minute + other.minute + second // 60
        hour = self.hour + other.hour + minute // 60
        return Time(hour % 24, minute % 60, second % 60)
    
    def display(self):
        print(self.hour,"Hour",self.minute,"minute",self.second,"second")

a,b,c=map(int,input("Enter time in format of hh mm ss:").split())
x,y,z=map(int,input("Enter 2nd time in format of hh mm ss:").split())



time1 = Time(a, b, c)
time2 = Time(x, y,z)

result = time1 + time2
result.display()
