import sys

num = list(sys.stdin.readline())
num = "".join(list(reversed(sorted(num))))

print(num)