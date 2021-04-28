# copyrightAvgMusic = copyrightMusic / totalMusic
# copyrightMusic = copyrightAvgMusic * totalMusic
# 23.53 == 24 = 894 / 38
totalMusic, copyrightAvgMusic = map(int,input().split(" "))
print(totalMusic * (copyrightAvgMusic-1) + 1)