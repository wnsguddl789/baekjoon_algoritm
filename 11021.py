T = int(input())
list_num = []
for i in range(T):
    A, B = map(int,input().split(" "))
    list_num.append([A,B])
for i in range(T):
    print('Case #{}: {}'.format(i+1,(
        list_num[i][0] + list_num[i][1]
        )))