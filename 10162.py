T = int(input())
# A 300s | B 60s | C 10s
A,B,C = 300,60,10
cond = int(((T%A)%B)%C)
if cond == 0:       print(int(T/A), int((T%A)/B), int(((T%A)%B)/C))
else:               print(-1)
