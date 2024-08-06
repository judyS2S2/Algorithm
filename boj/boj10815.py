### 백준 10815. 숫자카드
# 상근이가 숫자 카드 갖고 있는지 아닌지 확인
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

# 숫자 카드 개수
n = int(input())
# 숫자 카드의 숫자
cards = sorted(map(int, input().split()))
# 비교할 숫자 개수
m = int(input())
# 비교할 숫자
candidate = list(map(int, input().split()))

# 각 숫자에 대해 존재여부 확인
for target in candidate:
    # 존재하면 1, 없으면 0
    print(1 if binary(cards, target) else 0, end = ' ')