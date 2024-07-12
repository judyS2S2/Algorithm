### 백준 15651 N과 M (3)
# 중복가능하게 n개에서 m개 뽑기
import sys
input = sys.stdin.readline
# n, m 입력
n, m = map(int, input().split())

# 현재 선택된 숫자 저장할 리스트 생성
answer = []

# 재귀 함수 정의
def solution():
    # 선택한 숫자의 길이가 m이면 출력
    if len(answer) == m:
        print(*answer)
        return
    
    # 1부터 n에 대해 반복
    for i in range(1, n+1):
        # 숫자 선택
        answer.append(i)
        # 다음 숫자 선택 위한 재귀 호출
        solution()
        # 다음 경우 탐색 위해 선택된 숫자 제거
        answer.pop()

# 함수 실행
solution()