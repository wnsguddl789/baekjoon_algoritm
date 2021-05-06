import sys

n = int(sys.stdin.readline())
list=[]
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    list.append([x,y])
for x,y in sorted(list):
    print(x,y)