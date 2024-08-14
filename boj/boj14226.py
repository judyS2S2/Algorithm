### 백준 14226. 이모티콘
# 이모티콘 화면에 만드는 데 걸리는 최소 시간 구하기
import sys
from collections import deque
input = sys.stdin.readline

# 목표 이모티콘 개수 입력
s = int(input())
# 이모티콘 수와 클립보드 상태를 기록하기 위한 배열 초기화
# 배열 크기를 s * 2 + 1로 설정
ch = [[0] * (s * 2 + 1) for _ in range(s * 2 + 1)]
# 초기상태 : (화면 이모티콘 수, 클립보드 이모티콘 수, 시간)
q = deque([[1, 0, 0]])

# 큐 빌 때까지 순회
while q:
    # 현재 상태 큐에서 꺼냄
    bg, cl, time = q.popleft()

    # 현재 화면의 이모티콘 수가 목표 s와 같다면
    if bg == s:
        # 걸린 시간 출력 및 종료
        print(time)
        break
    
    # 이미 방문한 상태라면
    if ch[bg][cl]:
        # 다음 반복으로 넘어감
        continue

    # 현재 상태 방문 처리
    ch[bg][cl] = 1

    # 화면 이모티콘 수가 1 이상인 경우
    # 화면에 이모티콘이 있다면
    if bg >= 1:
        # 삭제 연산 (화면 이모티콘 수 1 감소, 시간 1초 증가)
        q.append([bg - 1, cl, time + 1])
        # 복사 연산 (클립보드에 현재 이모티콘 수 복사, 시간 1초 증가)
        # 화면 이모티콘 수 최대 1000개, 복사 가능 최대 1000개 => 2*s
        if bg <= s * 2:
            q.append([bg, bg, time + 1])
    
    # 클립보드에 이모티콘 있으면
    if cl:
        # 붙여넣기 연산 (화면 이모티콘 수 증가, 시간 1초 증가)
        # 화면 + 복붙했을 때, 총 2*s개로 인덱스 한정
        if bg + cl <= s * 2:
            q.append([bg + cl, cl, time + 1])