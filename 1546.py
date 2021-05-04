import sys

N = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))
max_score = max(score)

new_score = []
for i in range(N): 
        new_score.append(score[i]/max_score * 100)
print(sum(new_score)/N)