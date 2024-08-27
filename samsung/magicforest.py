### 삼성기출. 마법의 숲 탐색
# 각 정령이 텀색 완료 후 최종 위치한 행 번호 합 계산
import sys
from collections import deque
input = sys.stdin.readline

# 방향 이동 정의
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 입력 처리 및 초기화
# n : 행, m : 열, k : 정령 수
n, m, K = map(int,input().split())
# 숲의 상태 저장할 2차원 배열
a = [[0] * m for _ in range(n)]
# 최종 위치의 행 번호 합 저장할 변수
ans = 0

# 출구 위치 반환
def getExit(x, y, d):
    if d == 0: # 북
        return [x-1, y]
    elif d == 1: # 동
        return [x, y+1]
    elif d == 2: # 남
        return [x+1, y]
    else: # 서
        return [x, y-1]

# 좌표가 보드 내에 있는지 확인
def inBoard(nx, ny):
    if 0 <= nx < n and 0 <= ny < m:
        return True
    return False

# 골렘이 특정 좌표로 이동 가능한지 확인
def check(x, y):
    if not inBoard(x, y): # 좌표가 보드 밖이면
        if x < n and 0 <= y < m: # 좌표가 위쪽이 뚫린 바구니 같은 공간에 있는지
            return True
    else: # 좌표가 보드 안에 위치하면
        if a[x][y] == 0: # 다른 골렘이 없는지
            return True
    return False

# 골렘 이동
def move(c, d, no):
    global a
    # 골렘 내 중앙의 정령 위치. 보드 맨 위에서 두 칸 위인 x==-2 지점부터 내려온다.
    x, y = -2, c
    while True:
        # 남쪽으로 이동
        if check(x+2, y) and check(x+1, y-1) and check(x+1, y+1):
            x += 1
        # 서쪽으로 회전하며 이동
        elif check(x+1, y-1) and check(x-1, y-1) and check(x, y-2) and check(x+1, y-2) and check(x+2, y-1):
            x += 1
            y -= 1
            d = (d-1) % 4 # 반시계 방향 회전
        # 동쪽으로 회전하며 이동
        elif check(x+1, y+1) and check(x-1, y+1) and check(x, y+2) and check(x+1, y+2) and check(x+2, y+1):
            x += 1
            y += 1
            d = (d+1) % 4 # 시계 방향으로 회전
        else:
            break

    # 골렘 이동 완료 후 상태 확인
    if not inBoard(x, y) or not inBoard(x + 1, y) or not inBoard(x-1, y) or not inBoard(x, y+1) or not inBoard(x, y-1):
        return [False, -1, -1] # 숲 벗어난 경우
    else:
        # 골렘 숲에 표시
        a[x][y] = a[x+1][y] = a[x-1][y] = a[x][y+1] = a[x][y-1] = no
        ex, ey = getExit(x, y, d) # 출구 위치
        a[ex][ey] = -no # 출구 음수 표시
        return [True, x, y]

# 정령 이동
def bfs(sx, sy, no):
    global ans

    cand = [] # 남쪽으로 이동 가능한 칸 후보리스트
    q = deque()
    q.append((sx, sy)) # 시작위치 큐에 삽입
    visit = [[False] * m for _ in range(n)] # 방문체크
    visit[sx][sy] = True

    while q:
        # 현재 위치 큐에서 꺼내기
        x, y=q.popleft()
        # 상하좌우 탐색
        for k in range(4):
            nx, ny=x + dx[k], y + dy[k]
            if not inBoard(nx, ny) or visit[nx][ny] or a[nx][ny] == 0:
                continue
            # 절댓값이 같은 칸으로 움직이거나, 출구 칸에서 다른 칸으로 이동 가능
            if abs(a[x][y]) == abs(a[nx][ny]) or (a[x][y] < 0 and abs(a[nx][ny]) != abs(a[x][y])):
                q.append((nx, ny))
                visit[nx][ny] = True
                cand.append(nx) # 이동 가능한 칸 추가

    # 가장 남쪽을 우선으로 정렬
    cand.sort(reverse = True)
    # 가장 남쪽 칸의 위치
    point = cand[0] + 1
    return point

# 정렬 이동 시뮬레이션
for no in range(1, K+1):
    c,d = map(int, input().split())
    # 0-index로 조정
    c -= 1

    # 골렘 이동
    res = move(c, d, no)
    inBound, x, y = res

    # 골렘 몸 일부가 숲 벗어나있는지 확인
    if inBound:
        # 정령 이동 및 행 번호 합산
        ans += bfs(x, y, no)
    else:
        # 골렘 숲 벗어나면 숲 초기화
        a=[[0] * m for _ in range(n)]

# 최종 결과 출력
print(ans)