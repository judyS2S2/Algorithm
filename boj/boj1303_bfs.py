### 백준 1303. 전쟁 - 전투_bfs
# 우리 팀 병사의 위력과 적국의 병사의 위력 출력
# n명 뭉쳐있을 때의 위력 : n^2
import sys
from collections import deque
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
# bfs 통해 병사 그룹의 크기 계산
def bfs(x, y, color):
    # 그룹에 속한 병사 수 초기화
    cnt = 1
    # 큐 초기화 및 시작 병사 지정 및 방문 처리
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    # 큐가 빌 때까지 순회
    while q:
        # 큐에서 좌표 꺼내기
        x, y = q.popleft()

        # 네 방향에 대해 새로운 좌표 계산
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 범위 안에 있고 색깔이 같고 방문 X
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == color and visited[nx][ny] == 0:
                # 큐에 추가
                q.append((nx, ny))
                # 방문 처리
                visited[nx][ny] = 1
                # 새 병사 방문할 때마다 카운트 증가
                cnt += 1
    return cnt

# 병사 위력 변수 초기화
w, b = 0, 0

# 전체 범위 탐색하며 위력 계산
for i in range(m):
    for j in range(n):
        # 흰색이고 방문 X
        if graph[i][j] == 'W' and visited[i][j] == 0:
            # 흰색에 대해 bfs 함수 실행 및 위력 계산
            w += bfs(i, j, 'W') ** 2
        # 파란색이고 방문 X
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            # 파란색에 대해 bfs 함수 실행 및 위력 계산
            b += bfs(i, j, 'B') ** 2

# 그룹별 위력 총합 계산
print(w, b)