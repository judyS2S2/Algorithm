### 백준 2606. 바이러스_dfs
# 컴퓨터가 바이러스에 걸렸을 때, 해당 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력
import sys
input = sys.stdin.readline

# 컴퓨터의 수 입력
n = int(input())
# 간선 (직접 연결) 수 입력
v = int(input())

# 컴퓨터 연결 정보 저장할 그래프 초기화
graph = [[] for _ in range(n+1)]
# 방문 여부 초기화
visited = [0] * (n+1)

# 간선 정보에 따라 그래프 구성
for i in range(v):
    a, b = map(int, input().split())
    # a에 b 연결
    graph[a].append(b)
    # b에 a 연결 (양방향)
    graph[b].append(a)

# dfs 함수 정의
def dfs(v):
    # 현재 컴퓨터 방문 처리
    visited[v] = 1
    # 현재 컴퓨터와 연결된 다른 컴퓨터 확인
    for nx in graph[v]:
        # 방문 X
        if visited[nx] == 0:
            # 재귀적으로 함수 호출
            dfs(nx)

# 1번 컴퓨터부터 dfs 실행
dfs(1)
# 1번 컴퓨터를 통해 바이러스 걸린 컴퓨터 수 출력(자신 제외)
print(sum(visited) - 1)