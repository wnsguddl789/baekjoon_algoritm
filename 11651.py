import sys

n = int(sys.stdin.readline())
list=[]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    list.append([y,x])
for x,y in sorted(list):
    print(y,x)