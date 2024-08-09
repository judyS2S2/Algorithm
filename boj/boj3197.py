### 백준 3197. 백조의 호수
# 며칠이 지나야 백조들이 만날 수 있는지 계산
import sys
from collections import deque
input = sys.stdin.readline
# 행과 열의 개수 입력
r, c = map(int, input().split())
# 호수의 상태 입력 -> 리스트로 저장
board = [list(input().strip()) for _ in range(r)]

# 이동 방향 정의
dx = [-1, 1, 0, 0] # 열 이동 : 위, 아래
dy = [0, 0, -1, 1] # 행 이동 : 왼쪽, 오른쪽

# 백조를 찾는 함수
def find_swan(swan_q, swan, visited, board):
    # 다음 위치 저장할 큐
    swan_nextq = deque()
    # 백조의 위치가 담긴 큐가 빌 때까지 순회
    while swan_q:
        # 현재 백조 위치 꺼냄
        y, x = swan_q.popleft()
        # 현재 백조의 위치와 두번째 백조 위치 같다면
        if y == swan[1][0] and x == swan[1][1]:
            # 만남 표시하고 종료
            return True, None
        
        # 상하좌우로 이동하며 탐색
        for k in range(4):
            # 새로운 좌표 계산
            ny, nx = y + dy[k], x + dx[k]
            # 새로운 좌표가 범위 내에 있고 방문 X
            if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == 0:
                # 새로운 위치가 얼음이라면
                if board[ny][nx] == 'X':
                    # 다음 백조 위치 큐에 추가
                    swan_nextq.append([ny, nx])
                else:
                    # 물이라면 백조의 이동 큐에 추가
                    swan_q.append([ny, nx])
                visited[ny][nx] = 1 # 방문 처리
    # 다음 백조 위치 큐 반환
    return 0, swan_nextq

# 얼음이 녹는 함수
def melt_ice(water_q, board):
    # 다음 물 위치를 저장할 큐 초기화
    water_nextq = deque()
    # 현재 물 위치가 담긴 큐 빌 때까지 순회
    while water_q:
        # 현재 물 위치 꺼내기
        y, x = water_q.popleft()
        # 상하좌우 탐색하며 얼음 녹이기
        for k in range(4):
            # 새로운 좌표 계산
            ny, nx = y + dy[k], x + dx[k]
            # 범위 체크
            if 0 <= ny < r and 0 <= nx < c:
                # 새로운 위치가 얼음이라면
                if board[ny][nx] == 'X':
                    # 다음 물 위치 큐에 추가
                    water_nextq.append([ny, nx])
                    # 얼음 녹임
                    board[ny][nx] = "."
    # 다음 물 위치 큐 반환
    return water_nextq

# 전체적인 해결 로직 포함하는 함수 정의
def solution(board):
    # 물 위치를 저장할 큐 초기화
    water_q = deque()
    # 백조 위치 저장할 리스트 초기화
    swan = []
    # 경과 일수 초기화
    day = -1
    # 방문 여부 체크 위한 배열 초기화
    visited = [[0] * c for _ in range(r)]

    # 호수 상태 확인하면서 초기 큐와 백조 위치 설정
    for row in range(r):
        for col, val in enumerate(board[row]):
            # 물이나 백조라면
            if val == "." or val == "L":
                # 물 위치 큐에 추가
                water_q.append([row, col])
            # 백조의 위치라면
            if val == "L":
                # 백조 위치 저장
                swan.append([row, col])

    # 백조 위치 저장할 큐 초기화
    swan_q = deque()
    # 첫번째 백조 위치 가져옴
    y, x = swan[0][0], swan[0][1]
    # 첫번째 백조 위치 큐에 추가
    swan_q.append([y, x])
    # 첫번째 백조 위치 방문 처리
    visited[y][x] = 1

    while True:
        # 하루 증가
        day += 1
        # 백조 찾기
        found_flag, swan_nextq = find_swan(swan_q, swan, visited, board)
        # 만났다면 루프 종료
        if found_flag: break
        # 얼음 녹이기
        water_q = melt_ice(water_q, board)
        # 다음 백조 위치 큐로 업데이트
        swan_q = swan_nextq
    # 경과 일수 반환
    return day
# 결과 출력
print(solution(board))