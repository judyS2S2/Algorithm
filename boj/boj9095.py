### 백준 9095. 1, 2, 3 더하기
# n을 1, 2, 3의 합으로 나타내는 방법의 수
import sys
input = sys.stdin.readline
# 테스트 케이스 입력
t = int(input())
# 테스트케이스 동안 n 입력 및 dp 초기화
for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)

# 1부터 n까지 순회
    for i in range(1, n + 1):
        # i = 1인 경우, 1가지
        if i == 1:
            dp[i] = 1
         # 2인 경우, 2가지
        elif i == 2:
            dp[i] = 2
        # 3인 경우, 4가지
        elif i == 3:
            dp[i] = 4
        # 4 이상이면 점화식 정의
        # a_i = a_i-1 + a_i-2 + a_i-3
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    # 결과 출력
    print(dp[n])