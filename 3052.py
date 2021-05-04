import sys
list = []
for i in range(10):
    num = int(sys.stdin.readline())
    list.append(num%42)
print(len(set(list)))