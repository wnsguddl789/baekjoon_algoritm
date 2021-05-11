import sys
from itertools import combinations
word = sys.stdin.readline().rstrip()
candidates = [i for i in range(1, len(word))]
comb_candiates = list(combinations(candidates,2))
res = "z"*len(word)

for comb_candiate in comb_candiates:
    split1,split2 = comb_candiate[0],comb_candiate[1]
    temp1 = word[:split1][::-1]
    temp2 = word[split1:split2][::-1]
    temp3 = word[split2:][::-1]
    temp = temp1 + temp2 + temp3
    if temp < res:
        res = temp
print(res)