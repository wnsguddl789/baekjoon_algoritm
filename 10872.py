import sys
N = int(sys.stdin.readline())
total=1
for i in range(N):
    total *= (i+1)
print(total)