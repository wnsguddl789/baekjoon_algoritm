import sys

N = int(sys.stdin.readline())
arr = [ ["*"]* N for _ in range(N) ]

v = N;cnt = 0
while v!=1:
    v/=3
    cnt+=1

for cnt_ in range(cnt):
    idx = [ i for i in range(N) if (i // 3 ** cnt_) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j] = " "

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))