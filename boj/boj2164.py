### 백준 2164. 카드2
# 큐/덱을 활용해서 카드 맨 위 버리고 그다음 숫자 맨 아래 추가하는 기능 수행
from collections import deque
import sys
input = sys.stdin.readline

# 입력값 : 카드 범위
N = int(input())

# 함수 정의
def cards(N):
    # 덱에 저장
    d = deque(range(1, N + 1))

    # 카드 1개이면 종료
    while len(d) > 1:
        # 맨 위 카드 버림
        d.popleft()
        # 버린 후, 그 다음 숫자 pop한 뒤 append
        d.append(d.popleft())
    # 반복문 빠져나오면, 즉 카드 1개이면 카드 번호 반환
    return d[0]

print(cards(N))