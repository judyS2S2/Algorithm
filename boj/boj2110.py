### 백준 2110. 공유기 설치
# 가장 인접한 두 공유기 사이의 최대 거리 출력
import sys
input = sys.stdin.readline
# 집의 수와 공유기 수 입력
n, c = map(int, input().split())
# 각 집의 좌표 리스트에 입력받아 저장
arr = list(int(input()) for _ in range(n))
# 집의 좌표 오름차순 정렬
arr.sort()
# 공유기 사이의 최소/최대 거리 초기화
start, end = 1, arr[-1] - arr[0]

# 이진탐색 반복문
while start <= end:
    # 중간값(공유기 사이의 거리 후보) 계산
    mid = (start + end) // 2
    # 첫번째 집에 공유기 설치
    current = arr[0]
    # 설치된 공유기 수 초기화
    count = 1

    # 나머지 집들 순회하며 공유기 설치
    for i in range(1, len(arr)):
        # 현재 집 좌표 >= 마지막 공유기 설치 위치 + 중간값 이상
        if arr[i] >= current + mid:
            # 공유기 설치
            count += 1
            # 현재 위치 업데이트
            current = arr[i]
    # 설치된 공유기 개수 >= 목표 개수
    if count >= c:
        # 더 큰 거리로 탐색
        start = mid + 1
    # 설치된 공유기 개수 < 목표 개수
    else:
        # 더 작은 거리로 탐색
        end = mid - 1

# 인접한 두 공유기 최대 거리 출력
print(end)