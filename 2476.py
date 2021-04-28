T = int(input())
dice_list, sorted_dice_list, reward= [], [], []
for i in range(T):
    dice = list(map(int,input().split()))
    dice_list.append(dice)
    sorted_dice_list.append(sorted(dice_list[i],reverse=True))
    # 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
    if sorted_dice_list[i][0] == sorted_dice_list[i][2]:
        reward.append(10000+int(sorted_dice_list[i][0])*1000)
    # 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
    elif sorted_dice_list[i][0] == sorted_dice_list[i][1] or sorted_dice_list[i][1] == sorted_dice_list[i][2]:
        reward.append(1000+sorted_dice_list[i][1]*100)
    # 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
    elif sorted_dice_list[i][0] != sorted_dice_list[i][1] and sorted_dice_list[i][1] != sorted_dice_list[i][2]:
        reward.append(max(sorted_dice_list[i])*100)

print(max(reward))