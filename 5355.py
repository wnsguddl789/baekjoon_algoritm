import sys
T = int(sys.stdin.readline())

for i in range(T):
    testSet = list(sys.stdin.readline().split()); num = float(testSet.pop(0))
    for j in range(len(testSet)):
        if   testSet[j] == "@": num *= 3
        elif testSet[j] == "%": num += 5
        elif testSet[j] == "#": num -= 7
    print("{:.2f}".format(num))