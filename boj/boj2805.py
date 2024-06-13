### boj 2805 나무 자르기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# map에서는 [] 말고, list()로 묶어줘야 함
trees = list(map(int, input().split()))
# 이분탐색 범위(기준) 설정
left, right = 1, max(trees)

# 적절한 나무 길이 찾는 알고리즘
while left <= right:
    # 중간값 계산
    mid = (left + right) // 2
    # 벌목된 나무 총합 초기화
    sum = 0

    # 중간값 기준으로 잘랐을 때, 가져갈 수 있는 나무 길이 총합 계산
    for i in trees:
        if i >= mid:
            sum += i - mid
    
    # 벌목 높이 이분탐색
    # 가져갈 수 있는 나무 길이 합이 목표보다 크거나 같으면
    if sum >= m:
        # 높이를 높여야 함
        left = mid + 1
    # 가져갈 수 있는 나무 길이 합이 목표보다 작으면
    else:
        # 높이를 낮춰야 함
        right = mid - 1

# 최대 높이 구하는 것이므로 right 도출
print(right)