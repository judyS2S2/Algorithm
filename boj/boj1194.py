### 백준 1194. 달이 차오른다, 가자
# 민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값 구하기
import sys
from collections import deque
input = sys.stdin.readline
# 미로 크기 입력
n, m = map(int, input().split())
# 미로 구조 입력 -> 2중 리스트로 저장
board = [list(input().rstrip()) for _ in range(n)]

# 상하좌우 이동 위한 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 문에 대응하는 열쇠 있는지 확인
def haveKey(cur_key, door):
    # 현재 키와 문이 맞는지 비트 연산으로 확인
    value = cur_key & (1 << (ord(door) - ord('A')))
    # 키가 있으면 True, 없으면 False 반환
    return True if value else False

# bfs 통한 미로탐색
def bfs(x, y):
    # 큐에 시작 위치, 이동 카운트, 갖고 있는 키를 추가
    q = deque([(x, y, 0, 0)])
    # 방문 체크 배열 초기화
    check = [[[False] * (1 << 6) for _ in range(50)] for _ in range(50)]
    # 시작 위치 방문 처리
    check[x][y][0] = True

    # 큐가 빌 때까지 순회
    while q:
        # 큐에서 현재 위치와 이동 카운트, 키를 꺼냄
        x, y, cnt, key = q.popleft()
        # 출구에 도착하면
        if board[x][y] == '1':
            # 이동 카운트 반환
            return cnt
        # 상하좌우로 이동
        for k in range(4):
            # 새로운 위치 계산
            nx, ny = x + dx[k], y + dy[k]
            # 범위 내에 있고 방문 X
            if 0 <= nx < n and 0 <= ny < m and not check[nx][ny][key]:
                # 출구 또는 빈 공간이면
                if board[nx][ny] == '1' or board[nx][ny] == ".":
                    # 방문 처리
                    check[nx][ny][key]  = True
                    # 큐에 추가
                    q.append((nx, ny, cnt + 1, key))
                # 열쇠 발견한 경우
                elif 'a' <= board[nx][ny] <= 'f':
                    # 열쇠 추가
                    tmp_key = key | (1 << (ord(board[nx][ny]) - ord('a')))
                    # 방문 처리
                    check[nx][ny][tmp_key] = True
                    # 큐에 추가
                    q.append((nx, ny, cnt + 1, tmp_key))
                # 문을 발견한 경우
                elif 'A' <= board[nx][ny] <= 'F':
                    # 키가 있는지 확인
                    if haveKey(key, board[nx][ny]):
                        # 방문 처리
                        check[nx][ny][key] = True
                        # 큐에 추가
                        q.append((nx, ny, cnt + 1, key))
    # 탈출할 수 없는 경우 -1 반환
    return -1

# 입력받은 미로에서 민식이의 시작 위치 탐색
for i in range(n):
    for j in range(m):
        # 현재 위치가 '0'인 경우
        if board[i][j] == '0':
            # 시작 위치 저장
            sx, sy = i, j
            # 시작 위치 빈 공간으로 변경
            board[i][j] = "."

# bfs 실행하여 결과 출력
print(bfs(sx, sy))