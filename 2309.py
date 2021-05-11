import sys
hobbit = []
for _ in range(9):
    hobbit.append(int(sys.stdin.readline()))
sum_hobbit = sum(hobbit)
one,two = 0,0
for i in range(8):
    for j in range(i+1,9):
        if sum_hobbit - (hobbit[i] + hobbit[j]) == 100:
            one = hobbit[i];two = hobbit[j]
hobbit.remove(one);hobbit.remove(two);hobbit.sort()
for i in hobbit:print(i)