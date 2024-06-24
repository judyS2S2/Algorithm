### 백준 2178. 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline
#n, m 입력
n, m = map(int, input().split())
# 그래프 초기화
graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

# bfs 함수 정의
def bfs(x, y):
    # 이동할 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
   # 큐 초기화, (x, y)부터 시작
    q = deque()
    q.append((x, y))
    # 큐 빌 때까지 순회
    while q:
        # 큐의 첫번째 요소 꺼내서 x, y(현재 위치)에 저장
        x, y = q.popleft()
        # 네가지 방향 위치 확인
        for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              # 범위 확인
              if 0<= nx < n and 0<= ny < m:
                # 경로 확인
                if graph[nx][ny]==1:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기
    return graph[n-1][m-1]
print(bfs(0,0))