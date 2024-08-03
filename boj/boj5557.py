### 백준 5557. 1학년
# 숫자가 주어졌을 때, 만들 수 있는올바른 등식의 수 구하기
import sys
input = sys.stdin.readline

# 숫자의 개수 입력
n = int(input())
# 숫자 배열 입력
nums = list(map(int, input().split()))
# dp 테이블 초기화, dp[i][j]는 i번째 숫자까지 사용해서 값 j를 만드는 경우의 수
dp = [[0] * 21 for _ in range(n)]
# 초기값 설정, 첫번째 숫자로 만들 수 있는 유일한 값
dp[0][nums[0]] = 1

# 두번째 숫자부터 마지막 숫자 전까지 반복
for i in range(1, n - 1):
    # 0부터 20까지 중간 계산값 반복
    for j in range(21):
        # 이전 숫자까지 j를 만들 수 있는 경우
        if dp[i - 1][j]:
            # 더한 결과가 20 이하인 경우
            if j + nums[i] <= 20:
                # j + nums[i]가 20 이하인 경우에만 값 업데이트
                dp[i][j + nums[i]] += dp[i - 1][j]
            # 뺀 결과가 0 이상인 경우
            if j - nums[i] >= 0:
                # 음수인 경우 올바른 등식X
                # j - nums[i]가 0 이상인 경우에만 값 업데이트
                dp[i][j - nums[i]] += dp[i - 1][j]

# 마지막 숫자를 목표값으로 만드는 경우의 수 출력
print(dp[n - 2][nums[-1]])