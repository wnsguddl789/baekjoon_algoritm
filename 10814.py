import sys

N = int(sys.stdin.readline())
account_list = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    account_list.append((int(age),name,i))
account_list.sort(key= lambda account:(account[0],account[2]))

for account in account_list:
    print(account[0],account[1])