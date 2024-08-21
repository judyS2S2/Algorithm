### 백준 10422. 괄호
# 각 테스트 케이스에 대해 길이가 L인 올바른 괄호 문자열의 개수를 나눈 나머지 출력
import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력
t = int(input())
# 각 테스트 케이스마다 괄호 문자열의 길이 입력
l = list(int(input()) for _ in range(t))

# dp 초기화 : 길이 5000까지의 올바른 괄호 문자열 개수 저장
dp = [0] * 5001
# 길이 0인 올바른 괄호 문자열의 개수는 1 (빈 문자열)
dp[0] = 1

# 길이가 짝수인 경우만 확인 (홀수는 올바른 괄호 문자열 X)
for i in range(2, 5001, 2):
    # 부분 문자열들을 분할해서 dp값을 계산
    for j in range(2, i + 1, 2):
        # dp 점화식
        dp[i] += (dp[i - 2] * dp[i - j]) % 1000000007

# 각 테스트 케이스에 대해
for i in l:
    # 길이가 l인 올바른 괄호 문자열의 개수를 나눈 나머지 출력
    print(dp[i] % 1000000007)