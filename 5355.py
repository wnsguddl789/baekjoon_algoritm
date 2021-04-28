T = int(input())
# @ = num * 3
# % = num + 5
# # = num - 7

def rhfqoddl(num):
    num = int(num) * 3
    return num
def vjtpsxm(num):
    num = num + 5
    return num
def tiv(num):
    num = num - 7
    return num

list = []
for i in range(T):
    string = input()
    list.append(string.split(" "))

    # num, firstOp, secondOp, thirdOp = input().split(" ")
    # list.append([num,firstOp,secondOp,thirdOp])

for i in range(T):
    if len(list[i]) == 2:
        num = list[i][0:1]
        firstOp = list[i][1:2]
        print(firstOp == "@")
        if firstOp == "@":
            print(num * 3)
    elif len(list[i]) == 3:
        print(list[i][1:2])
    elif len(list[i]) == 4:
        print(list[i][1:2])