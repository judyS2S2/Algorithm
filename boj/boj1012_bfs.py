### 백준 1012. 유기농 배추
# 상하좌우로 서로 인접해있는 배추밭에서 지렁이 최소 수 구하기
import sys
from collections import deque
input = sys.stdin.readline
# 테스트 케이스 입력
t = int(input())

# 방향 설정 (동/서/남/북)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs 함수 정의
def bfs(visited, x, y):
    # 큐 초기화 및 초기 정점 설정
    queue = deque()
    queue.append([x, y])
    # 방문 처리 : 방식 -> 1을 0으로 바꾸기
    visited[x][y] = 0

    # 큐가 빌 때까지 순회
    while queue:
        # 큐의 첫번째 요소 꺼내서 저장
        x, y = queue.popleft()

        # 네 방향에 대해 탐색 수행
        for i in range(4):
            # 현재 위치로부터 새로운 위치 게산
            nx = x + dx[i]
            ny = y + dy[i]

            # 배추밭 벗어나지 않는지 확인
            if 0<= ny < n and 0 <= nx < m:
                # 배추가 있다면
                if visited[nx][ny] == 1:
                    # 큐에 추가
                    queue.append([nx, ny])
                    # 방문 처리 : 방식 -> 1을 0으로 바꾸기
                    visited[nx][ny] = 0

# 테스트 케이스 동안 입력 단계 수행
for _ in range(t):
    # m, n, k 입력
    m, n, k = map(int, input().split())
    # 빈 배추밭
    visited = [[0] * (n) for _ in range(m)]
    # K줄에 걸쳐 배추 위치 주어짐
    for _ in range(k):
        a, b = map(int, input().split())
        # 배추 위치 표기
        visited[a][b] = 1
    
    # 지렁이 수 초기화
    count = 0
    
    # 모든 좌표에 대해 bfs 수행
    for j in range(m):
        for k in range(n):
            # 배추가 있으면
            if visited[j][k] == 1:
                # bfs 수행
                bfs(visited, j, k)
                # 지렁이 개수 1씩 증가
                count += 1
    # 결과 출력
    print(count)