import sys
n = int(sys.stdin.readline())
num = [0,1]
for i in range(n):
    new = 0
    for j in range(len(num)):
        new += num[j]
    num.pop(0);num.append(new)
print(num[0])