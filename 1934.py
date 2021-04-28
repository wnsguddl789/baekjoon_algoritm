from math import gcd

def lcm(x,y):
    return x * y // gcd(x,y)

T = int(input())
for i in range(T):
    A,B = map(int, input().split())
    print(lcm(A,B))
