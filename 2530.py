Hour , Min , Sec= map(int,input().split(" "))
reqTime = int(input())

Sec = Sec + reqTime
Min = (Min + Sec / 60) % 60
Hour = (Hour + Min / 60) % 24

print(int(Hour),int(Min % 60),Sec%60)

Hour , Min = map(int,input().split(" "))
reqTime = int(input())

Min = Min + reqTime
Hour = (Hour + Min / 60) % 24

print(int(Hour),Min % 60)