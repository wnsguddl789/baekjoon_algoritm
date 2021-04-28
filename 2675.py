# t = int(input())
# for i in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)

num = int(input())
for i in range(num):
    n, s = input().split()
    text = [int(n) * i for i in s]
    print("".join(text))
    # list = []
    # list.append("".join(text))
    # print(list)