### 백준 1743. 음식물 피하기_bfs
# 인접한 음식물끼리 합쳐지는데 가장 큰 음식물 크기 구하기
import sys
from collections import deque
input = sys.stdin.readline
# 통로의 세로 ,가로, 음식물 개수 입력
n, m, k = map(int, input().split())
size = []   # 음식물 크기 저장할 리스트
# 통로 나타내는 2차원 리스트 (초기화 -> 0)
graph = [[0] * m for _ in range(n)]
# 음식물 개수만큼 좌표 입력받기
for _ in range(k):
    r, c = map(int, input().split())
    # 입력받은 좌표에 음식물 표시
    graph[r-1][c-1] = 1

# 동서남북 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    # 현재 음식물 크기
    res = 0
    # 큐 초기화 및 시작점 설정 및 음식물 방문 처리 0 -> 재방문 방지
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    # 큐 빌 때까지 순회
    while q:
        # 큐에서 좌표 꺼내기
        x, y = q.popleft()
        # 덩어리 크기 증가
        res += 1
        # 네 방향 탐색하여 인접한 칸 확인
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 범위 내에 있고 음식물이 있으면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 큐에 추가
                q.append((nx, ny))
                # 방문 처리 0 -> 재방문 방지
                graph[nx][ny] = 0
    return res  # 현재 음식물 덩어리 크기 반환

# 전체 범위 순회
for i in range(n):
    for j in range(m):
        # 음식물이 있다면
        if graph[i][j] == 1:
            # 함수 실행하여 덩어리 크기를 size에 추가
            size.append(bfs(i, j))

# 가장 큰 음식물 덩어리 크기 출력
print(max(size))