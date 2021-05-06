import sys
from collections import Counter

N = int(sys.stdin.readline());list=[]

for i in range(N):
    num = int(sys.stdin.readline());list.append(num)

def modefinder(list):
    c = Counter(list)
    order = c.most_common()
    maximum = order[0][1]

    modes= []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

print(round(sum(list) / N))
# 1: 산술평균 : N개의 수들의 합을 N으로 나눈 값
print(sorted(list)[int(len(list) / 2)])
# 2: 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
if len(modefinder(list)) == 1: print(modefinder(list)[0])
else: print(sorted(modefinder(list))[1])
 # 3: 최빈값 : N개의 수들 중 가장 많이 나타나는 값
print(max(list) - min(list)) 
# 4: 범위 : N개의 수들 중 최댓값과 최솟값의 차이