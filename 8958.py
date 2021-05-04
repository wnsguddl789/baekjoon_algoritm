import sys
from collections import Counter
T = int(sys.stdin.readline())
for i in range(T):
    ox = list(sys.stdin.readline())
    score = 0
    pop_list = []
    print(len(ox))
    for j in range(len(ox)): 
        if ox[j] == "X": 
            pop_list.append(j)
            print(j)
    for j in range(len(pop_list)): ox.pop(j)
    ox.pop()
    print(ox)