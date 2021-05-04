while True:
    n = int(input())
    if n==-1: break

    list_num = []
    for i in range(1,n+1):
        if n%i == 0 : list_num.append(i)

    sum_l = 0
    sum_r = list_num[len(list_num)-1]
    for i in list_num[:-1]:
        sum_l += i
    if sum_l == sum_r:
        answer = str(sum_r)+ " = " + str(list_num[0])
        for i in range(1,len(list_num)-1):
            answer+=" + "+str(list_num[i])
        print(answer)
    else:
        print(str(list_num[-1])+" is NOT perfect.")
        
    # set_num = set(list_num)
    # list_set_num = list(set_num)
    # list_set_num.pop()
    # num_list = []
    # for i in range(len(list_set_num)):
    #     num_list.append(list_set_num[i])
    #     print(num_list[i],end=" ")
    # print()
    # for i in range(len(list_set_num)):
    #     if sum(num_list) == n:
    #         if i==0:
    #             print(n,"=",num_list[i],end="")
    #         else:
    #             print(" +",num_list[i],end="")
    #     else:
    #         print("{} is NOT perfect.".format(n),end="")

    # print()
    