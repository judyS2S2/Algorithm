### 백준 1182. 부분수열의 합
# 주어진 합이 되는 부분수열의 개수 출력
import sys
input = sys.stdin.readline

# 정수의 개수 및 목표 합 입력
n, s = map(int, input().split())
# 정수 입력받아 리스트로 저장
nums = list(map(int, input().split()))
# 부분 수열 개수 초기화
cnt = 0
# 현재 부분 수열 저장 위한 리스트 초기화
ans = []

# 부분 수열 찾기 위한 재귀 함수 정의
def solve(start):
    # cnt 전역변수로 사용 -> 재귀호출 간 값 유지
    global cnt
    # 현재 부분수열의 합이 s와 같고, 크기가 양수인 부분수열이면
    if sum(ans) == s and len(ans) > 0:
        # 카운트 증가
        cnt += 1

    # start부터 n까지 반복하여 부분수열 생성
    # start 통해 이미 선택한 원소 다시 선택 X, 중복 X
    for i in range(start, n):
        # 현재 수 부분수열에 추가
        ans.append(nums[i])
        # 다음 인덱스에서 재귀 호출
        solve(i + 1)
        # 마지막에 추가한 수 제거 (백트래킹)
        ans.pop()

# 재귀함수 호출 및 초기값으로 0 넘김
solve(0)
# 결과로 카운트 출력
print(cnt)