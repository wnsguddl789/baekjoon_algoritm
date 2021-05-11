import sys
# 97 122
S = sys.stdin.readline().rstrip()
for i in range(25):
    for j in S:
        print(chr(97+i),end=" ")