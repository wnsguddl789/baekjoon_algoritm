score = []
sum = 0
for i in range(5):
    num = int(input())
    if num < 40:
        score.append(40)
        sum += 40
    else:
        score.append(num)
        sum += num
    
avg = int(sum / len(score))
print(avg)