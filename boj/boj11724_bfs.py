### 백준 11724. 연결 요소의 개수
# 방향 없는 그래프에서 연결 요소의 개수 구하기
import sys
from collections import deque
input = sys.stdin.readline
# 정점과 간선 입력
n, m = map(int, input().split())
# 노드의 개수만큼 빈 리스트 가지는 리스트 생성 -> 그래프 초기화
graph = [[] for _ in range(n+1)]

# m개의 간선 정보 입력 -> 그래프 구성
for i in range(m):
    # u, v 입력
    u, v = map(int, input().split())
    # u -> v
    graph[u].append(v)
    # v -> u : 무방향 조건 처리
    graph[v].append(u)

# 연결 요소의 개수 초기화
count = 0
# 방문 여부 확인 리스트 초기화
visited = [0] * (n+1)

# bfs 함수 정의
def bfs(graph, start, visited ):
    # 큐 초기화 및 시작노드 설정
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = 1

    # 큐가 빌 때까지 순회
    while queue:
        # 큐의 첫번째 요소 꺼내서 v에 저장
        v = queue.popleft()

        # 꺼낸 노드에 인접한 노드 확인
        for i in graph[v]:
            # 인접한 노드 방문 X
            if visited[i] == 0:
                # 큐에 인접 노드 추가
                queue.append(i)
                # 해당 노드 방문 처리
                visited[i] = 1 

# 모든 노드 순회하며 연결 요소 개수 계산
for i in range(1, n+1):
    # 현재 노드 방문 X
    if visited[i] == 0:
        # bfs 수행하며 연결된 모든 노드 방문 처리
        bfs(graph, i, visited)
        # 연결 요소의 개수 1씩 증가
        count += 1

# 연결 요소의 개수 출력
print(count)