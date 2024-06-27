### 백준 11047. 동전 0
# 동전의 합 K를 만들기 위해 필요한 최소 동전 개수
import sys
input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())

# 동전 가치 저장할 리스트 생성
coins = []

# n줄 동안 동전 입력 및 리스트에 저장
for _ in range(n):
    coins.append(int(input()))

# 동전 개수 초기화
count = 0

# 동전 가치 내림차순 정렬
coins.sort(reverse = True)

# 동전과 목표금액 비교하여 작으면 반복문 수행, 아니면 종료
for coin in coins:
    # 목표금액 >= 화폐가치
    if k>= coin:
        # 개수에 나눈 몫 더해주기
        count += k // coin
        # 나머지 할당하여 반복문 진행
        k %= coin
        
        # 목표금액 <= 0이면 종료
        if k <= 0:
            break

# 동전 개수 출력
print(count)