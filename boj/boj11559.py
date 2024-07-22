### 백준 11559. Puyo Puyo
# 블록 상하좌우 탐색 후, 4개 이상인 같은 블록 제거 후, 총 몇 번 제거하는지 횟수 계산
import sys
from collections import deque
input = sys.stdin.readline

# 동서남북 방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 12x6 크기의 필드 정보 입력받기
board = [list(input().rstrip()) for _ in range(12)]
# 연쇄 횟수
combo = 0

# 동서남북으로 동일한 블록들 탐색해 해당 좌표 가진 리스트 반환
def bfs(x, y):
    # 큐 초기화
    q = deque()
    # 시작점 정의
    q.append((x, y))
    # 시작점 방문 처리
    visited[x][y] = 1

    # 동일한 블록 좌표 담을 리스트에 현재 블록 좌표 추가
    same_blocks = [(x, y)]
    # 큐가 빌 때가지 순회
    while q:
        # 큐에서 좌표 꺼내기
        x, y = q.popleft()
        # 네 방향 탐색 및 새로운 좌표 정의
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 범위 설정 (좌표 유효하고, 같은 색이며, 방문X)
            if 0 <= nx < 12 and 0 <= ny < 6 and board[x][y] == board[nx][ny] and visited[nx][ny] == 0:
                # 큐에 추가
                q.append((nx, ny))
                # 방문 처리
                visited[nx][ny] = 1
                # 동일 블록 리스트에 추가
                same_blocks.append((nx, ny))
    # 동일 블록 리스트 반환
    return same_blocks

# 동일한 블록들 제거
def delete(same_blocks):
    for x, y in same_blocks:
        # 블록을 빈 공간으로 변경
        board[x][y] = "."

# 역순으로 반복문 돌며 위에서 아래로 블록 내림
def down():
    # 각 열에 대해
    for y in range(6):
        # 아래에서 위로 (역순으로) 탐색
        # 10부터 시작하는 이유 : 11행은 가장 아래 행이고, 위에 있는 블록을 아래로 내리므로 10행부터 시작
        for x in range(10, -1, -1):
            # x 위치 위의 행을 탐색 -> x에서 k위치로 블록 내리기
            # k는 11부터 x+1까지 감소
            # 역순으로 탐색하여 빈 공간이 있으면 그 위의 블록 아래로 내림
            for k in range(11, x, -1):
                # 블록이 있고, 아래가 빈 공간이면
                if board[x][y] != "." and board[k][y] == ".":
                    # 아래로 블록 이동
                    board[k][y] = board[x][y]
                    # 원래 위치를 빈 공간으로 변경
                    board[x][y] = "."

while True:
    # 이번 턴에 터진 블록이 있는지 여부
    pang = False
    # 방문 여부 초기화
    visited = [[0] * 6 for _ in range(12)]

    # 모든 필드 탐색
    for x in range(12):
        for y in range(6):
            # 블록이 있고 방문하지 않았다면
            if board[x][y] != "." and visited[x][y] == 0:
                # bfs로 동일 블록 좌표 얻기
                same_blocks = bfs(x, y)

                # 동일한 블록이 4개 이상인 경우 블록 제거
                if len(same_blocks) >= 4:
                    # 블록 터짐 처리
                    pang = True
                    # 블록 제거
                    delete(same_blocks)
    
    # 터뜨릴 블록이 있다면, 블록 제거하고 밑으로 내리기
    if pang:
        # 블록 내리기
        down()
        # 연쇄 횟수 증가
        combo += 1
    else:
        # 터질 블록이 없으면 종료
        break

# 연쇄 횟수 출력
print(combo)