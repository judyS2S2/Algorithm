### 백준 7576. 토마토
# 토마토가 모두 익을 때까지의 최소 날짜 출력
import sys
from collections import deque
input = sys.stdin.readline
# 상자의 가로 칸 수 m, 세로 칸 수 n 입력
m, n = map(int, input().split())
# n줄 동안 상자의 상태 입력받아 2차원 리스트에 저장
box = [list(map(int, input().split())) for _ in range(n)]

# 왼/오/앞/뒤
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 위한 큐 초기화
q = deque([])
# 전체 박스에서 익은 토마토 있다면 위치를 큐에 추가
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

def bfs():
    # 큐가 빌 때까지
    while q:
        # 큐에서 토마토 꺼냄
        x, y = q.popleft()
        # 네 방향으로 탐색
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 범위 안에 있고 익지 않은 토마토라면
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                # 익음 처리 (날짜 증가)
                box[nx][ny] = box[x][y] + 1
                # 새로운 위치 큐에 추가
                q.append([nx, ny])
# 함수 실행
bfs()
# 결과 변수 초기화
result = 0

for tomato in box:
    for t in tomato:
        # 아직 익지 않은 토마토가 있다면 
        if t == 0:
            # -1 출력하고 종료
            print(-1)
            exit(0)
    
    result = max(result, max(tomato))

# 시작을 1로 했으므로 1을 빼서 출력
print(result - 1)