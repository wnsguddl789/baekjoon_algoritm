import collections

dice = [x for x in map(int,input().split())]
length_set_dice  = len(set(dice))
length_list_dice = len(dice)
duplicated_item = [item for item, count in collections.Counter(dice).items() if count > 1]
print(duplicated_item)
print((duplicated_item))
print(length_list_dice,length_set_dice)
print(length_list_dice - length_set_dice)
if length_list_dice - length_set_dice == 0:
    print(10000 + duplicated_item * 1000)
if length_set_dice - length_set_dice == 1:
    print(1000 + duplicated_item * 100)
if length_list_dice - length_set_dice == 2:
    print(max(dice) * 100)