import sys

# 연료 소비율은 단위시간당 소비하는 연료의 양
# c = f / per 1Hour
# N 우주선 개수 / D 목적지 까지의 거리  
# v 최고속도 / f 우주선의 연료양 / c 연료소비율

T = int(sys.stdin.readline())
for _ in range(T):
    N,D = map(int,sys.stdin.readline().split());result = 0
    for _ in range(N):
        v,f,c = map(int,sys.stdin.readline().split())
        if f / c * v >= D: 
            result += 1
    print(result)