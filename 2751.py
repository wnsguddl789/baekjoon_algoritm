import sys

N = int(sys.stdin.readline());list=[]
for i in range(N):
    num = int(sys.stdin.readline())
    list.append(num)
list = (sorted(list))

for i in list:
    print(i)
    