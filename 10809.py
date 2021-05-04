import sys
# 97 122
S = sys.stdin.readline()
for i in range(25):
    for j in S:
        if j == chr(97+i):print(chr(97+i),end=" ")