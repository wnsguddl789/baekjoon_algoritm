#  1 <= N <= 10^6    
N = int(input())
step = 0

while True:
    if N == 1: break
    print(N,end=" ")
    if N % 3 ==0:
        N = int(N / 3);print(N,end=" ")
    elif N % 2 == 0:
        N = int(N / 2);print(N,end=" ")
    else: N = N - 1;print(N,end=" ")
