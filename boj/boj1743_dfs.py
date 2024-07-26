### 백준 1743. 음식물 피하기_dfs
# 인접한 음식물끼리 합쳐지는데 가장 큰 음식물 크기 구하기
import sys
sys.setrecursionlimit(10000)  # 재귀 한도를 늘려서 많은 재귀 호출을 허용
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

n, m, k = map(int, input().split())  # 통로의 세로 길이, 가로 길이, 음식물 쓰레기 개수 입력
size = []  # 음식물 크기들을 저장할 리스트
graph = [[0] * m for _ in range(n)]  # 통로를 나타내는 2차원 리스트 (초기에는 모두 0)

for _ in range(k):
    r, c = map(int, input().split())  # 음식물 쓰레기 좌표 입력
    graph[r-1][c-1] = 1  # 입력 받은 좌표에 음식물 표시 (1)

dx = [1, -1, 0, 0]  # 상하좌우 이동을 위한 x축 변화량
dy = [0, 0, 1, -1]  # 상하좌우 이동을 위한 y축 변화량

def dfs(x, y):
    stack = [(x, y)]  # DFS를 위한 스택
    res = 0  # 현재 음식물 덩어리의 크기 초기화
    while stack:
        x, y = stack.pop()
        if graph[x][y] == 1:  # 음식물 쓰레기가 있으면
            graph[x][y] = 0  # 방문한 음식물은 0으로 변경하여 재방문 방지
            res += 1  # 덩어리 크기 증가
            for i in range(4):  # 상하좌우로 인접한 칸 확인
                nx = dx[i] + x  # 새로운 x 좌표
                ny = dy[i] + y  # 새로운 y 좌표
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    stack.append((nx, ny))  # 스택에 추가
    return res

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 음식물이 있는 좌표에서 DFS 시작
            size.append(dfs(i, j))  # DFS 결과 (덩어리 크기)를 size 리스트에 추가

print(max(size))  # 가장 큰 음식물 덩어리의 크기 출력