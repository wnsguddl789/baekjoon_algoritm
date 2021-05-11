import sys
from math import sqrt
def data_in():
    return map(int,sys.stdin.readline().split())

def solution( _diff):
    if _diff == 0: return 0
    lower = sqrt( _diff)
    if lower == int(lower): 
        return lower * 2 - 1
    return int(lower) * 2 if _diff < int(lower) ** 2 + lower else int(lower) * 2 + 1 
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        X,Y = data_in()
        ans = solution(abs(X - Y))
        print(int(ans))

# if _diff < int(lower) ** 2 + lower:
#     return int(lower) * 2
# else:
#     return int(lower) * 2 + 1       

# return int(lower) * 2 if _diff < int(lower) ** 2 + lower else int(lower) * 2 + 1 

# if(int(integer_str_value) > 0):
#             return True
#         else:
#             return False

# return True if int(integer_str_value) > 0 else False