T = int(input())
list_num = []
for i in range(T):
    A, B = map(int,input().split(" "))
    list_num.append([A,B])
for i in range(T):
    index = i + 1
    num_1 = list_num[i][0]
    num_2 = list_num[i][1]
    result = num_1 + num_2
    print('Case #{}: {} + {} = {}'.format(index,num_1,num_2,result))
        