### 백준 12851. 숨바꼭질 2
# 수빈이가 동생을 찾는 가장 빠른 시간 구하기
import sys
from collections import deque

# 수빈이와 동생 위치 입력
n, k= map(int, sys.stdin.readline().split())

# 큐 초기화 및 수빈이 위치 시작점 추가
q = deque()
q.append(n)

# 각 위치까지의 최단 시간 기록할 배열 초기화
way = [0]*100001

# 결과 시간 및 방법의 수 초기화
cnt, result = 0, 0

# 큐 빌 때까지 순회
while q:
    # 현재 위치 큐에서 꺼내기
    a =  q.popleft()
    temp = way[a]

    # 동생 위치 도달하면
    if a == k:
        result = temp # 최단 시간 업데이트
        cnt += 1    # 방법의 수 증가
        continue
    
    # 수빈이가 이동할 수 있는 세 가지 경우에 대해 탐색
    for i in [a-1, a+1, a*2]:
        # 다음 위치가 범위 내에 있고 방문 X or 같은 시간에 방문 가능한 경우
        if 0 <= i < 100001 and (way[i] == 0 or way[i]== way[a] +1): #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
            way[i] = way[a] + 1 # 다음 시간까지 최단 시간 업데이트
            q.append(i) # 다음 위치 큐에 추가
# 결과 출력
print(result)
print(cnt)