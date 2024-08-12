### 백준 13549. 숨바꼭질 3
# 수빈이가 동생을 찾는 가장 빠른 시간 구하기
import sys
from collections import deque
input = sys.stdin.readline

# 수빈이와 동생의 위치 입력
n, k = map(int, input().split())
# 큐 초기화 및 수빈이 위치 시작점 추가
q = deque([n])

# 각 위치까지의 최단 시간 기록할 배열 초기화
time = [-1] * 100001
# 수빈이의 시작 위치는 0초
time[n] = 0

# bfs 수행
while q:
    # 수빈이의 현재 위치 큐에서 꺼내기
    a = q.popleft()

    # 동생 위치 도달하면
    if a == k:
        # 최단 시간 출력 및 종료
        print(time[a])
        break
    
    # 수빈이가 이동할 수 있는 세 가지 경우에 대해
    for i in (a - 1, a + 1, a * 2):
        # 범위 내에 있고 방문 X
        if 0 <= i <100001 and time[i] == -1:
            # 순간이동
            if i == a * 2:
                # 순간이동은 시간 추가 X
                time[i] = time[a]
                # 큐의 앞에 추가하여 우선 처리
                q.appendleft(i)

            # 걷기
            else:
                # 걷는 경우는 1초 추가
                time[i] = time[a] + 1
                # 큐의 뒤에 추가
                q.append(i)