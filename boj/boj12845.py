### 백준 12845. 모두의 마블
# 카드를 합쳐 받을 수 있는 골드의 최댓값 구하기
import sys
input = sys.stdin.readline
# 카드의 개수 입력
n = int(input())
# 카드의 레벨 리스트에 입력
cards = list(map(int, input().split()))

# 내림차순 정렬
cards.sort(reverse = True)

# 정렬한 레벨 첫번째 값 level에 저장
level = cards[0]

# 결과 골드값 초기화
gold = 0

# 두번째 카드부터 순차적으로 합성하여 골드값 누적
for i in range(1, len(cards)):
    gold += level + cards[i]

# 결과값 출력
print(gold)