### 백준 2281. 데스노트
# 이름을 쓸 때 각 줄별로 뒤의 여백을 구하는 문제
import sys
input = sys.stdin.readline

# 이름의 수, 노트 너비 입력
n, m = map(int, input().split())
# 각 사람의 이름의 길이 입력받아 리스트에 저장
names = [int(input()) for _ in range(n)]
# dp 초기화
# dp[r][c]는 r번째 이름까지 작성했을 때, c만큼 남는 칸들의 제곱합 최솟값
dp = [[-1] * (m+1) for _ in range(n)]
# 첫번째 이름을 적고 나서 여백이 남지 않을 경우 제곱합 0
dp[0][names[0]] = 0

# 모든 이름에 대해 순차적으로 처리
for r in range(n-1):
    # 각 줄에 대해 가능한 모든 여백의 경우 검사
    for c in range(1, m+1):
        # 유효한 상태인지 확인(초기화 -1)
        if dp[r][c] != -1:
            # 현재 줄에 다음 이름 추가할 수 있는지 확인
            if c + 1 + names[r+1] <= m:
                # 여백이 그대로 있는 경우 다음 줄에 업데이트
                dp[r+1][c+names[r+1]+1] = dp[r][c]
            
            # 현재 줄에서 다음 이름을 새로 적는 경우 고려
            # 이미 값이 있다면 최솟값 갱신
            if dp[r+1][names[r+1]] != -1:
                dp[r+1][names[r+1]] = min(dp[r+1][names[r+1]], dp[r][c] + (m-c)**2)
            else:   # 처음 값이 들어가는 경우
                dp[r+1][names[r+1]] = dp[r][c] + (m-c) ** 2

# 최솟값 구하기 위해 큰 값으로 초기화
answer = 1000000000
# 마지막 줄을 제외한 여백의 최소 제곱합 찾기
for i in range(1, m+1):
    if dp[n-1][i] != -1:
        answer = min(answer, dp[n-1][i])

print(answer)