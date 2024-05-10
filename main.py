# Scenario
# Create a class representing a time interval;
# the class should implement its own method for addition, subtraction on time interval class objects;
# the class should implement its own method for multiplication of time interval class objects by an integer-type value;
# the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
# the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
# check the argument type, and in case of a mismatch, raise a TypeError exception
# Test data:

# the first time interval (fti) is hours=21, minutes=58, seconds=50
# the second time interval (sti) is hours=1, minutes=45, seconds=22
# the expected result of addition (fti + sti) is 23:44:12
# the expected result of subtraction (fti - sti) is 20:13:28
# the expected result of multiplication (fti * 2) is 43:57:40
#################################################################################################################################


class myTime:
    def __init__(self, hour, min, seg):
        self.timeStamp = self.turnTimeStamp(f"{hour}:{min}:{seg}")
        self.initTime()

    def turnTimeStamp(self, time: str):
        lis = time.split(sep=":")
        if (
            len(lis) != 3
            or not lis[0].isnumeric()
            or not lis[1].isnumeric()
            or not lis[2].isnumeric
        ):
            raise TypeError
        return int(lis[0]) * 3600 + int(lis[1]) * 60 + int(lis[2])
        # lis [0] = hours
        # lis [1] = minutes
        # lis [2] = seconds

    def turnTimeFormat(self, timeStamp: int):
        currentNum = timeStamp
        hours = currentNum // 3600
        currentNum %= 3600
        minutes = currentNum // 60
        currentNum %= 60
        seconds = currentNum
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def initTime(self):
        self.hours = self.timeStamp // 3600
        self.minutes = self.timeStamp % 3600 // 60
        self.seconds = self.timeStamp % 3600 % 60

    def __str__(self):
        return self.turnTimeFormat(self.timeStamp)

    def __add__(self,other):
        return self.turnTimeFormat(self.timeStamp + other.timeStamp)
    def __sub__(self,other):
        return self.turnTimeFormat(self.timeStamp - other.timeStamp)
    def __mul__(self,other):
        if hasattr(other,"timeStamp"): return self.turnTimeFormat(self.timeStamp * other.timeStamp)
        return self.turnTimeFormat(self.timeStamp * other)

firsInterval = myTime(21,58,50)
secondInterval = myTime(1,45,22)

print(firsInterval)
print(secondInterval)
print(firsInterval + secondInterval)
print(firsInterval - secondInterval)
print(firsInterval * 2)