### 백준 1303. 전쟁 - 전투_dfs
# 우리 팀 병사의 위력과 적국의 병사의 위력 출력
# n명 뭉쳐있을 때의 위력 : n^2
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# 전쟁터의 크기 입력
n, m = map(int, input().split())
# 그래프 초기화(병사 배치)
graph = [list(input().strip()) for _ in range(m)]
# 방문여부 초기화
visited = [[0] * n for _ in range(m)]
# 방향 설정
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

# dfs 통해 병사 그룹 크기 계산
def dfs(x, y, color):
    # 시작 병사 방문 처리
    visited[x][y] = 1
    # 현재 병사 수 설정
    cnt = 1

    # 네 방향에 대해 새로운 좌표 계산
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        # 범위 안에 있고 색깔이 같고 방문 X
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == color and visited[nx][ny] == 0:
            # 재귀 호출하여 그룹 크기 증가
            cnt += dfs(nx, ny, color)
    return cnt

# 병사 위력 변수 초기화
w, b = 0, 0

# 전체 범위 탐색
for i in range(m):
    for j in range(n):
        # 흰색이고 방문 X
        if graph[i][j] == 'W' and visited[i][j] == 0:
            # dfs 함수 실행하여 위력 계산
            w += dfs(i, j, 'W') ** 2
        # 파란색이고 방문 X
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            # dfs 함수 실행하여 위력 계산
            b += dfs(i, j, 'B') ** 2

# 그룹별 위력 총합 출력
print(w, b)