### 백준 1697. 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline
# 수빈, 동생 위치 입력
n, k = map(int, input().split())
# 문제 조건 중 최댓값 처리
MAX = 10 ** 5
# 방문리스트 초기화
visited = [0] * (MAX + 1)

# bfs 함수 정의
def bfs(n):
    # 큐 초기화, n부터 시작
    q = deque([n])
    # 큐 빌 때까지 순회
    while q:
        # 큐의 첫번째 요소 꺼내서 x(현재 위치)에 저장
        x = q.popleft()
        # 현재 위치가 동생의 위치와 같다면
        if x == k:
            # 현재 위치 도달한 시간 출력 및 종료
            print(visited[x])
            break
        # 현재 위치에서 이동할 수 있는 3가지 경우
        for nx in (x-1, x+1, 2*x):
            # 위치가 범위 내에 있고, 방문X
            if 0 <= nx <= MAX and visited[nx] == 0:
                # 방문 리스트에 현재 위치까지의 시간 기록
                visited[nx] = visited[x] + 1
                # 다음 위치 큐에 추가
                q.append(nx)
                
# bfs 수행, n부터 탐색 시작
bfs(n)