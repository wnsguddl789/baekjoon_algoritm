Hour , Min = map(int,input().split(" "))
reqTime = int(input())

def convertTime(hour,min):
    if hour == 24: hour = 0
    if min  == 60: min  = 0
    return hour,min
def plusOneHour(hour):
    hour = hour + 1
    if hour == 24: hour = 0
    return hour

Hour,Min = convertTime(Hour,Min)

if Min + reqTime < 60:
    Min = Min + reqTime
elif Min + reqTime >= 60:
    if Min + reqTime == 60:
        Min = 0
        Hour = plusOneHour(Hour)
    if Min + reqTime > 60:
        Min = (Min + reqTime) % 60
        if (Min + reqTime) / 60 == 1: Hour = plusOneHour(Hour)
        elif (Min + reqTime) / 60 > 1:
            Hour = Hour + (int((Min + reqTime) / 60))
            if Hour >=24 : Hour = Hour - 24
print(Hour,Min)