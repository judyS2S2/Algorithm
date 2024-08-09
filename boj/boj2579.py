### 백준 2579. 계단오르기
# 게임에서 얻을 수 있는 총 점수의 최댓값 구하기
import sys
input = sys.stdin.readline
# 계단 개수 입력
n = int(input())
# 계단 점수 저장할 배열 초기화
stairs = [0] * 301
# 각 계단의 점수 입력받아 배열에 저장
for i in range(1, n + 1):
    stairs[i] = int(input())

# 최대 점수 저장할 배열 초기화
dp = [0] * 301
# 첫번째 계단의 최대 점수는 그 계단의 점수
dp[1] = stairs[1]
# 두 개인 경우 최대 점수는 두 계단의 합
dp[2] = stairs[1] + stairs[2]
# 세 개인 경우 두 가지 경우 중 큰 값
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 네번째 계단부터 n번째까지 최대 점수 계산
for i in range(4, n + 1):
    # 1. i-3번째 계단 밟고, i-1번째 계단 밟은 후 i번째 계단 밟는 경우
    # 2. i-2번째 계단 밟고 i번째 계단 밟는 경우
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

# 결과 출력
print(dp[n])