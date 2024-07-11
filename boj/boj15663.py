### 백준 15663. N과 M (9)
# n개의 자연수 중 m개의 자연수로 이루어진 길이 m 수열 구하되, 중복X, 오름차순 정렬
import sys
input = sys.stdin.readline
# n, m 입력
n, m = map(int, input().split())
# n개의 자연수 입력받아 정렬
num = sorted(list(map(int, input().split())))
# 방문 여부 확인
visited = [0] * n
# 현재까지 선택된 숫자를 저장하는 리스트
answer = []

def solution():
    # 이미 사용된 숫자 체크하기 위한 변수 초기화
    check = 0
    # 선택된 숫자가 m개가 되면
    if len(answer) == m:
        # 수열 출력
        print(*answer)
        return
    
    # n개의 숫자에 대해 반복
    for i in range(n):
        # 해당 숫자 사용X, 방문 X
        # 같은 숫자 다시 선택하지 않기 위한 조건 설정
        if check != num[i] and visited[i] == 0:
            # 숫자를 선택
            answer.append(num[i])
            # 해당 숫자 사용했음 표시
            visited[i] = 1
            # 현재 숫자를 변수에 저장
            check = num[i]
            # 다음 숫자 선택하기 위한 재귀 호출
            solution()
            # 선택한 숫자 다시 빼서 다음 경우 탐색
            answer.pop()
            # 해당 숫자 사용하지 않았음 표시
            visited[i] = 0

# 함수 실행
solution()