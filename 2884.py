H, M = map(int,input().split())
reqTime = 45

M = M - reqTime
H = (H + M / 60) % 24

print(int(H),M % 60)