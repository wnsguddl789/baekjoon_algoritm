import sys

dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
call = sys.stdin.readline()
ret = 0

for i in range(len(call)):
    for j in dial:
        if call[i] in j:
            ret += dial.index(j)+3
print(ret)