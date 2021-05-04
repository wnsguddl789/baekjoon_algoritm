# 734 893 -> 437 398
import sys
A,B = map(list,sys.stdin.readline().split())
A.reverse();A = "".join(A)
B = B.reverse();B = "".join(B)
if A > B: print(A)
else:print(B)