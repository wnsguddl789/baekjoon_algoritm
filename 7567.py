import sys
plate = sys.stdin.readline()
plate_length = len(plate)-2 # 4

stack = 10
for i in range(plate_length):
    if   plate[i] == plate[i+1]: stack +=5;
    elif plate[i] != plate[i+1]: stack += 10;
print(stack)