###백준 1654. 랜선 자르기
# k개의 랜선이 주어지고, 이 랜선들을 잘라서 n개의 랜선을 만들 수 있는 최대 길이 찾기
import sys
input = sys.stdin.readline
# k, n 입력
k, n = map(int, input().split())
# k줄에 걸쳐 랜선길이 입력
lan = [int(input()) for _ in range(k)]
# 이분탐색 범위 설정
left, right = 1, max(lan)

# 적절한 랜선 길이 찾기
while left <= right:
    # 중간값 계산
    mid = (left + right) // 2
    # 랜선 개수 초기화
    count = 0
    
    # 중간값 기준으로 잘랐을 때 몇 개의 랜선 만들 수 있는지 계산
    for i in lan:
        count += i // mid

    # 랜선 개수와 목표 개수 비교
    # 목표 개수 채웠으면
    if count >= n:
        # 더 길게 만들 수 있는지 확인 비교
        left = mid + 1
    # 목표 개수보다 적으면
    else:
        # 잘라서 더 짧은 길이로 시도
        right = mid - 1

# 최대 길이 구하므로 right 도출
print(right)