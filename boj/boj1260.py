### 백준 1260 DFS와 BFS
# 그래프 DFS, BFS 탐색 결과 출력 프로그램
# 첫째 줄에 DFS, 그 다음 줄에 BFS 결과 출력, 시작 : v
import sys
from collections import deque
input = sys.stdin.readline
# n : 정점 개수, m : 간선 개수, v : 시작 정점 번호
n, m, v = map(int, input().split())

# 인접 행렬로 그래프 초기화
graph = [[0]*(n+1) for _ in range(n+1)]

# 간선 정보 입력받아 인접 행렬에 저장
for i in range(m):
    a, b = map(int, input().split())
    # 양방향이므로 ab = ba
    graph[a][b] = graph[b][a] = 1

# 방문 리스트 초기화
# dfs 방문기록
visited1 = [0] * (n+1)
# bfs 방문기록
visited2 = [0] * (n+1)

# dfs 함수 정의
def dfs(v):
    # 현재 정점 방문 표시
    visited1[v] = 1
    # 현재 방문한 정점 출력
    print(v, end = ' ')

    # 모든 정점 확인
    for i in range(1, n+1):
        # 만약 해당 정점 방문X
        if visited1[i] == 0:
            # 현재 정점 v와 정점 i의 연결여부 확인
            if graph[v][i] == 1:
                # 연결 -> 해당 정점에 대해 dfs 재귀 호출
                dfs(i)

def bfs(v):
    # 큐 초기화, 시작 정점 큐에 삽입
    queue = deque([v])
    # 시작 정점 방문 처리
    visited2[v] = 1

    # 큐가 빌 때까지 반복
    while queue:
        # 큐의 첫번째 요소 꺼내서 변수 v에 저장
        v = queue.popleft()
        # 현재 방문한 정점 출력
        print(v, end = ' ')

        # 모든 정점 확인
        for i in range(1, n+1):
            # 만약 해당 정점 방문X
            if visited2[i] == 0:
                # 현재 정점 v와 정점 i의 연결여부 확인
                if graph[v][i] == 1:
                    # 연결 -> 큐에 해당 정점 추가
                    queue.append(i)
                    # 해당 정점 방문 표시
                    visited2[i] = 1
# dfs 함수 호출
dfs(v)
# 줄 바꿈
print()
# bfs 함수 호출
bfs(v)