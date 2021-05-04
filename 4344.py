import sys

C = int(sys.stdin.readline())

for i in range(C):
    score = list(map(int,sys.stdin.readline().split()))
    student = score[0];score.pop(0)
    avg = sum(score) / student;low = 0
    for j in score:
        if j > avg:low+=1
    print("{:.3f}%".format((low/student*100)))