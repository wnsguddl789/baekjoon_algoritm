# 카드의 합이 21을 넘지 않는 한도 내에서, 
# 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.
import sys

N,M = map(int,sys.stdin.readline().split())
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
card = list(map(int,sys.stdin.readline().split()))
print(sorted(card))