import sys

N = int(sys.stdin.readline())
num = list(sys.stdin.readline())
total = 0
for i in range(N): total += int(num[i])
print(total)