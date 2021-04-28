list = list(input().split(" "))

for i in range(len(list)):
    list[i] = int(list[i])

sorted_list = sorted(list,reverse=True)
print(sorted_list[1])