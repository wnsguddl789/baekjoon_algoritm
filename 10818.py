import sys

# 정수의 개수 N (1 ≤ N ≤ 1,000,000)
N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
print(min(num_list),max(num_list))