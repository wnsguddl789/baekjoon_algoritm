K , N , M = map(int,input().split())
pinMoney = M - (K * N)
if pinMoney > 0:    pinMoney = 0
else:               pinMoney = abs(pinMoney)
print(pinMoney)