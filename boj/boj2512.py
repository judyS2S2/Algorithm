### 백준 2512. 예산
# 배정된 예산들 중 최댓값 출력
import sys
input = sys.stdin.readline
# 지방의 수 입력
n = int(input())
# 각 지방 예산 요청 리스트로 저장
cities = list(map(int, input().split()))
# 총 예산
m = int(input())

# 이진 탐색 위한 초기 범위 설정
start, end = 1, max(cities)

while start <= end:
    # 중간값(상한액 후보) 계산
    mid = (start + end) // 2
    # 배정된 총 예산 초기화
    total = 0
    # 각 지방의 예산 요청을 순회하며 배정
    for i in cities:
        # 요청 금액 > 상한액
        if i > mid:
            # 상한액 배정
            total += mid
        else:
            # 요청 금액 < 상한액 -> 요청 금액 그대로 배정
            total += i
    # 배정된 총 예산 <= 총 예산
    if total <= m:
        # 더 큰 상한액 탐색
        start = mid + 1
    else:   # 배정된 총 예산 > 총 예산
        # 더 적은 상한액 탐색
        end = mid - 1

# 최종 상한액 출력
print(end)