import sys
V = int(sys.stdin.readline()) # 1 <= V <= 15
vote = list(sys.stdin.readline(V));cnt_A,cnt_B = 0,0
for i in range(V):
    if   vote[i] == "A": cnt_A += 1
    elif vote[i] == "B": cnt_B += 1
print(cnt_A,cnt_B)
if   cnt_A >  cnt_B:print("A")
elif cnt_A <  cnt_B:print("B")
elif cnt_A == cnt_B:print("Tie")