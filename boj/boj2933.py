### 백준 2933. 미네랄
# 모든 막대 던지고 난 후 미네랄 모양 구하기
import sys
from collections import deque
input = sys.stdin.readline

# 동굴의 크기 R행 C열
R, C = map(int, input().split())
# 동굴의 상태
room = [list(input().rstrip()) for _ in range(R)]
N = int(input())  # 막대를 던진 횟수
# 막대를 던진 높이들
throw = list(map(int, input().split()))
# 방향벡터 정의 (우, 좌, 하, 상)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    bomb = False  # 미네랄 파괴 여부
    start_x = R - throw[i]  # 던지는 높이 (행)

    if i % 2 == 0:  # 창영이 던지는 경우 (왼쪽에서 오른쪽)
        start_y = 0
        while start_y < C:
            # 미네랄 만나면
            if room[start_x][start_y] == "x":
                # 미네랄 파괴
                room[start_x][start_y] = "."
                # 파괴된 위치 저장
                bx, by = start_x, start_y
                # 미네랄 파괴 표시
                bomb = True
                break
            start_y += 1
    else:  # 상근이 던지는 경우 (오른쪽에서 왼쪽)
        start_y = C - 1
        while start_y >= 0:
            # 미네랄 만나면
            if room[start_x][start_y] == "x":
                # 미네랄 파괴
                room[start_x][start_y] = "."
                # 파괴된 위치 저장
                bx, by = start_x, start_y
                # 미네랄 파괴 표시
                bomb = True
                break
            start_y -= 1

    if not bomb:
        continue  # 미네랄이 파괴되지 않았으면 다음 턴으로 넘어감
    
    # 공중에 떠있는 클러스터 위치 저장
    cluster = []
    # 떨어지는 미네랄 위치 저장
    fall = []
    visited = [[0] * C for _ in range(R)]  # 방문 체크 배열

    # 바닥에 붙어있는 미네랄 체크 (BFS)
    for y in range(C):
        # 바닥에 있는 미네랄 중 방문 X
        if room[R-1][y] == "x" and not visited[R-1][y]:
            # 방문 처리
            visited[R-1][y] = 1
            # bfs 시작
            q = deque([[R-1, y]])
            while q:
                px, py = q.popleft()
                # 네 방향 탐색
                for d in range(4):
                    nx, ny = px + dx[d], py + dy[d]
                    # 범위 내에 있고, 방문 X, 미네랄 있으면
                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and room[nx][ny] == "x":
                        # 미네랄 위치 추가
                        q.append([nx, ny])
                        # 방문 처리
                        visited[nx][ny] = 1

    # 공중에 떠 있는 클러스터 체크 (BFS)
    for d in range(4):  # 파괴된 미네랄 주변 네 방향 탐색
        px, py = bx + dx[d], by + dy[d]
        # 공중에 떠있는 클러스터
        if 0 <= px < R and 0 <= py < C and room[px][py] == "x" and not visited[px][py]:
            visited[px][py] = 2 # 방문 체크
            q = deque([[px, py]])   # bfs 시작
            cluster.append([px, py]) # 클러스터 위치 저장
            room[px][py] = "." # 공중 클러스터 일시적 제거
            while q:
                px, py = q.popleft()
                # 아래 비었으면
                if room[px + 1][py] == ".":
                    # 떨어질 위치에 추가
                    fall.append([px, py])
                for d in range(4): # 네 방향 탐색
                    nx, ny = px + dx[d], py + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] == "x" and not visited[nx][ny]:
                        q.append([nx, ny])
                        visited[nx][ny] = 2
                        # 클러스터 위치 저장
                        cluster.append([nx, ny])
                        # 공중 클러스터 일시 제거
                        room[nx][ny] = "."

    # 최대 내려갈 수 있는 높이 계산
    if fall:
        under = False
        down = 1
        while True:
            for x, y in fall:
                if x + down >= R - 1 or (room[x + down + 1][y] == "x" and visited[x + down + 1][y]):
                    under = True
                    break
            if under:
                break
            down += 1

        # 클러스터를 내리기
        for nx, ny in cluster:
            room[nx + down][ny] = "x"

# 결과 출력
for row in room:
    print(''.join(row))