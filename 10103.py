n = int(input())
c_score,s_score = 100,100
for i in range(n):
    chanYoung , sangDeok = map(int,input().split())

    if      chanYoung < sangDeok:   c_score -= sangDeok
    elif    chanYoung > sangDeok:   s_score -= chanYoung
    elif    chanYoung == sangDeok:  continue
print(c_score)
print(s_score)