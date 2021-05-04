while True:
    try:
        num = list(input());cnt=0
        if len(num) == 1: num.insert(0,0)
        first_num = "".join(map(str,num))
        while True:
            new_num = 0
            for i in range(len(num)):
                new_num = new_num + int(num[i])
            new_num = new_num % 10
            num.append((new_num))
            num.pop(0)
            cnt +=1
            if "".join(map(str,num)) == first_num:
                print(cnt);break
    except EOFError:
        break