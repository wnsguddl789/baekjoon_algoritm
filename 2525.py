Hour , Min = map(int,input().split(" "))
reqTime = int(input())

Min = Min + reqTime
Hour = (Hour + Min / 60) % 24

print(int(Hour),Min % 60)