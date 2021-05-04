list=[]
for i in range(9):
    num = int(input())
    list.append([num,i+1])

print(max(list)[0])
print(max(list)[1])