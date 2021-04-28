A,B = 1,2
while True:
    A,B = map(int,input().split())
    if      A == 0 and B ==0:break
    elif    A >  B:          print("Yes")    
    elif    A <= B:          print("No")