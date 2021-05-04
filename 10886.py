N = int(input())
if N%2 !=0:
    cute,notcute = 0,0
    for i in range(N):
        iscute = int(input())
        if iscute == 1: cute +=1
        elif iscute == 0: notcute +=1

    if cute>notcute :print("Junhee is cute!")
    else :print("Junhee is not cute!")

