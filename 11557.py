T = int(input())
for i in range(T):
    N = int(input())
    dict_univ={}
    sojuList = []
    for j in range(N):
        univ, soju = input().split()
        sojuList.append(int(soju))
        dict_univ[int(soju)] = univ
    print(dict_univ[max(sojuList)])