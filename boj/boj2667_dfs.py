### 백준 2667. 단지번호 붙이기_dfs
import sys
input = sys.stdin.readline
# 지도의 크기 n
n = int(input())
# map 입력
map = [list(map(int, input().strip())) for _ in range(n)]
# 방문여부 bool[][](이중리스트)
visited = [[0] * n for _ in range(n)]
# 단지 크기 저장할 리스트 초기화
result = []
# 현재 단지 크기 저장할 변수 초기화
each = 0

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 한 칸씩 이동할 좌표 설정
# (x, y) => 동(1, 0), 서(-1, 0), 남(0, 1), 북(0, -1)
# 행렬 좌표 체계에서 행 : 위 -> 아래 증가, 열 : 왼 -> 오 증가
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# dfs 함수 정의
def dfs(x, y):
    # 전역변수로서의 값 유지 위해 global 선언
    # 전역변수 사용 -> 각 단지 크기 정확히 계산
    global each
    # 현재 단지의 크기 1 증가
    each += 1
    # 네 방향 (동/서/남/북)에 대해 탐색 수행
    for k in range(4):
        # 현재 위치(x, y)에서 특정 방향으로 한 칸 이동한 새로운 위치 계산
        nx = x + dx[k]
        ny = y + dy[k]
        # 지도 범위 벗어나지 않는지 확인
        # 2차원 리스트에서는 (행, 열) 순서 유지 -> (ny, nx)
        if 0 <= ny < n and 0 <= nx <n:
            # 집이 있고 아직 방문하지 않았다면
            if map[ny][nx] == 1 and visited[ny][nx] == 0:
                # 방문 처리
                visited[ny][nx] = 1
                # 해당 위치에서 dfs 재귀 호출
                dfs(nx, ny)

# 새로운 단지 있는지 전체 지도 순회하면서 탐색
for y in range(n):
    for x in range(n):
        # 집이 있고 아직 방문하지 않았다면
        if map[y][x] == 1 and visited[y][x] == 0:
            # 방문 처리
            visited[y][x] = 1
            # 현재 단지 크기 초기화
            each = 0
            # dfs 수행하여 단지 크기 계산
            dfs(x, y)
            # 단지 크기를 결과 리스트에 추가
            result.append(each)

# 단지 크기 오름차순 정렬
result.sort()
# 총 단지 수 출력
print(len(result))
# 각 단지의 크기를 한 줄씩 출력
for i in result:
    print(i)