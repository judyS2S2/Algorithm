### 백준 10816. 숫자 카드 2
# 숫자가 적혀있는 숫자카드를 상근이가 몇 개 가지고 있는지 구하기
import sys
input = sys.stdin.readline

# 상근이가 갖고 있는 숫자카드 개수 입력
n = int(input())
# 숫자카드에 적혀있는 숫자들 입력
cards = [*map(int, input().split())]
# 몇 개 갖고 있는지 구해야 할 숫자의 개수 입력
m = int(input())
# 몇 개 갖고 있는지 구해야 할 숫자들 입력
candidate = [*map(int, input().split())]

# 각 숫자카드의 개수 세기 위한 딕셔너리 생성
count = {}

for card in cards:
    if card in count:
        # 이미 있는 숫자면 1 증가
        count[card] += 1
    else:
        # 새로운 숫자면 1로 초기화
        count[card] = 1

# 구해야 할 숫자 각각에 대해 결과 출력
for target in candidate:
    # 딕셔너리에서 해당 숫자의 개수 가져옴, 없으면 0 출력
    result = count.get(target, 0)
    # 해당 숫자의 개수 출력
    print(result, end = " ")