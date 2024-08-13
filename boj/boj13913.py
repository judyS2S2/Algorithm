### 백준 13913. 숨바꼭질 4
# 수빈이가 동생을 찾는 가장 빠른 시간과 어떻게 이동해야 하는지 출력
import sys
from collections import deque
input = sys.stdin.readline

# 수빈이와 동생 위치 입력
n, k = map(int, input().split())

def bfs(n, k):
    # bfs 탐색 위한 큐 초기화
    q = deque([n])
    # 방문 여부 기록할 배열
    visited = [0] * 100001
    # 각 위치까지 도달하는 데 걸리는 시간
    distance = [0] * 100001
    # 각 위치에 도달하기 위해 이전에 방문한 위치 기록
    previous = [-1] * 100001

    # 수빈이의 시작 위치 방문처리
    visited[n] = 1
    # 동생 찾았는지 여부 초기화
    found = 0
    # 동생 찾는 데 걸리는 시간 초기화
    time = 0

    # 큐 빌 때까지 탐색
    while q:
        # 현재 큐 길이만큼 반복
        for _ in range(len(q)):
            # 현재 위치 큐에서 꺼내기
            a = q.popleft()

            # 동생 위치 도달하면
            if a == k:
                # 찾았다고 표시 및 종료
                found = 1
                break
            
            # 이동할 수 있는 경우에 대해 탐색
            for i in [a - 1, a + 1, 2 * a]:
                # 범위에 있고 방문 X
                if 0 <= i < 100001 and visited[i] == 0:
                    # 해당 위치 방문 처리
                    visited[i] = 1
                    # 시간 업데이트
                    distance[i] = distance[a] + 1
                    # 이전 위치 업데이트
                    previous[i] = a
                    # 다음 위치 큐에 추가
                    q.append(i)
        
        # 찾았다면
        if found:
            # 동생 찾은 후 걸린 시간 저장
            time = distance[a]
            break
    
    # 경로 추적 위한 리스트 초기화
    path = []
    # 현재 위치에서 시작하여 이전 위치 따라가며 경로 구성
    # previous = -1이면 이전 위치 없다는 뜻!
    while a != -1:
        # 현재 위치 경로에 추가
        path.append(a)
        # 이전 위치로 이동
        a = previous[a]

    # 경로 역순으로 정렬하여 올바른 순서로 만들기
    path.reverse()
    # 걸린 시간과 경로 반환
    return time, path

# 함수 실행
time, path = bfs(n, k)

# 결과 출력
print(time)
print(" ".join(map(str, path)))