import sys

while True:
    num_1 , num_2 = map(int,sys.stdin.readline().split())
    if num_1 == 0 and num_2 == 0: break

    elif num_1 < num_2: # 첫번쨰 수가 두번째 수의 약수일떄
        for i in range(num_2):
            if i == num_1:
                if num_2 % num_1 == 0:print("factor")
                elif num_2 % num_1 != 0:print("neither")
    elif num_1 > num_2: # 첫번쨰 수가 두번째 수의 배수일떄
        for i in range(num_1):
            if i == num_2:
                if num_1 % num_2 == 0:print("multiple")
                elif num_1 % num_2 != 0:print("neither")