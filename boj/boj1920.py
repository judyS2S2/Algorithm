### 백준 1920. 수 찾기
# N개의 정수 중 특정 정수 있는지 확인
import sys
input = sys.stdin.readline

# 이진 탐색 함수 통해 정렬된 리스트에서 특정 정수 존재하는지 확인
def binary(arr, x):
    # 탐색 범위를 배열 시작과 끝으로 설정
    start, end = 0, len(arr) - 1
    # 탐색 범위 유효한 동안 반복
    while start <= end:
        # 중간 인덱스 계산
        mid = (start + end) // 2
        # 중간값 < 찾는 값
        if arr[mid] < x:
            # 탐색 범위 오른쪽 절반으로 줄임
            start = mid + 1
        # 중간값 > 찾는 값
        elif arr[mid] > x:
            # 탐색 범위 왼쪽 절반으로 줄임
            end = mid - 1
        else:
            # 값을 찾으면 1 반환
            return 1
    # 못 찾으면 0
    return 0

# 입력 처리
n = int(input())
nums = sorted(map(int, input().split()))
m = int(input())
candidate = list(map(int, input().split()))

# 각 숫자에 대해 이진 탐색 결과 출력
for target in candidate:    # 각 후보 숫자에 대해
    # 존재하면 1, 아니면 0 출력
    print(1 if binary(nums, target) else 0)