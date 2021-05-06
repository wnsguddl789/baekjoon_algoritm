import sys

N = int(sys.stdin.readline());

x=list(map(int,sys.stdin.readline().split()))
sortX = sorted(list(set(sorted(x))))
dictX={}
for i in range(len(sortX)):
    dictX[sortX[i]] = i
print(dictX.values())
for i in range(len(sortX)):
    if i == dictX.values:
        print(1)
