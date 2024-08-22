### 백준 12869. 뮤탈리스크
# 모든 SCV 파괴하기 위해 공격해야 하는 최소 공격수
import sys
input = sys.stdin.readline

# scv 수 입력
n = int(input())
# 각 scv 체력 입력
scv = [*map(int, input().split())]
# scv가 3개가 아닐 경우를 대비해 0 추가해서 크기 맞추기
scv.extend([0, 0])

# dp 초기화, 해당 체력 만드는 데 필요한 최소 공격횟수
dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]
# 현재 scv 체력 상태 초기화
dp[scv[0]][scv[1]][scv[2]] = 1

# 가능한 공격 조합들 : (9, 3, 1) 방식으로 조합 다르게 공격
comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3)]

# 모든 가능한 체력 조합에 대해 탐색
# 첫번째 scv 체력 감소
for i in range(60, -1, -1):
    # 두번째 scv 체력 감소
    for j in range(60, -1, -1):
        # 세번째 scv 체력 감소
        for k in range(60, -1, -1):
            # 현재 상태가 유효할 때만 진행 (0 이하 자동 파괴)
            if dp[i][j][k] > 0:
                # 가능한 조합에 대해 순서대로 체력 감소
                for c in comb:
                    # 첫번째 scv 체력 감소(음수 방지)
                    i_ = i - c[0] if i - c[0] >= 0 else 0
                    # 두번째 scv 체력 감소(음수 방지)
                    j_ = j - c[1] if j - c[1] >= 0 else 0
                    # 세번째 scv 체력 감소(음수 방지)
                    k_ = k - c[2] if k - c[2] >= 0 else 0
                    # 새로운 상태에 대해 더 적은 공격으로 도달 가능할 때 갱신
                    if dp[i_][j_][k_] == 0 or dp[i_][j_][k_] > dp[i][j][k] + 1:
                        dp[i_][j_][k_] = dp[i][j][k] + 1

# 모든 scv를 파괴한 최소 공격 수 출력 (초기값 1이므로 -1)
print(dp[0][0][0] - 1)