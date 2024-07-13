### 백준 6987. 월드컵
# 각 나라의 승, 무, 패 가능한지 판별하기
import sys
input = sys.stdin.readline

# 경기 팀 이름과 인덱스 맵핑
team = ['A', 'B', 'C', 'D', 'E', 'F']
# 각 팀의 승/무/패 위치를 지정
position = {team[i]: i * 3 for i in range(6)}

# 모든 가능한 경기 조합 생성 (총 15개의 경기)
allMatch = [(i, j) for i in range(6) for j in range(i + 1, 6)]

# 각 경기 결과를 저장할 딕셔너리
result = {}

# 백트래킹 함수
# note : 현재까지의 경기 결과 기록 리스트
# depth : 현재까지 진행한 경기의 수
def match(depth, note):
    # 모든 경기를 다 탐색한 경우
    if depth == 15:
        # 현재 결과를 튜플로 변환하여 저장
        result[tuple(note)] = True
        # 종료
        return
    # 범위 설정
    for i in range(len(note)):
        # 현재 탐색 결과가 주어진 결과보다 큰 경우
        if note[i] > answer[i]:
            return
    
    # 현재 경기의 팀 인덱스 가져옴
    a, b = allMatch[depth]
    # 첫번째 팀 인덱스
    aIDX = a * 3
    # 두번째 팀 인덱스
    bIDX = b * 3

    # 첫번째 팀 승, 두번째 팀 패
    # 현재 결과 복사
    note_win = note[:]
    # 첫번째 팀 승리 증가
    note_win[aIDX] += 1
    # 두번째 팀 패배 증가
    note_win[bIDX + 2] += 1
    # 다음 경기로 이동
    match(depth + 1, note_win)

    # 첫번재 팀 무, 두번째 팀 무
    # 현재 결과 복사
    note_draw = note[:]
    # 첫번째 팀 무승부 증가
    note_draw[aIDX + 1] += 1
    # 두번째 팀 무승부 증가
    note_draw[bIDX + 1] += 1
    # 다음 경기로 이동
    match(depth + 1, note_draw)

    # 첫번째 팀 패, 두번째 팀 승
    # 현재 결과 복사
    note_lose = note[:]
    # 첫번째 팀 패배 증가
    note_lose[aIDX + 2] += 1
    # 두번째 팀 승리 증가
    note_lose[bIDX] += 1
    # 다음 경기로 이동
    match(depth + 1, note_lose)

# 입력과 결과 처리
# 4개의 결과 세트 입력받기
for _ in range(4):
    # 각 세트의 승/무/패 결과를 리스트로 변환
    answer = list(map(int, input().split()))
    # 백트래킹 함수 호출 및 초기화
    match(0, [0] * 18)
    # 결과 출력, 주어진 결과 가능한지 확인
    print(1 if tuple(answer) in result else 0, end=' ')