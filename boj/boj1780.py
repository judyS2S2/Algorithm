### 백준 1780. 종이의 개수
# 같은 숫자로만 채워진 각 숫자별 종이 개수 출력
import sys
input = sys.stdin.readline

# 행렬 크기 입력
n = int(input())

# 종이 크기 초기화
paper = []

# 종이 종류 초기화
# 딕셔너리 초기화 통해 각 상태 카운팅
result = {-1:0, 0:0, 1:0}

# 행렬 크기 동안 n개의 정수 입력
for _ in range(n):
    paper.append(list(map(int, input().split())))

# 종이의 종류(-1, 0, 1)와 다르면 쪼개기
def divided(row, col, n):
    # 종이 시작 지정
    current = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            # 현재 종이 종류와 다르다면
            if paper[i][j] != current:
                # 종이 1/3로 분할 (9->3->1)
                next = n // 3

                # 3x3그리드로 나누고 좌표 계산하여 재귀 호출
                # 종이를 같은 크기의 종이 9개로 분할
                divided(row, col, next) # 1번째 (0,0)
                divided(row, col+next, next) # 2번째 (0, 1)
                divided(row, col+(next*2), next) # 3번째(0, 2)
                divided(row+next, col, next) # 4번째 (1, 0)
                divided(row+next, col+next, next) # 5번째 (1, 1)
                divided(row+next, col+(next*2), next) # 6번째 (1, 2)
                divided(row+(next*2), col, next) # 7번째 (2, 0)
                divided(row+(next*2), col+next, next) # 8번째 (2, 1)
                divided(row+(next*2), col+(next*2), next) # 9번째 (2, 2)
                # 만약 현재 종이가 모두 같은 숫자 X 
                #-> 9개로 나누고 더 이상 나머지 부분 실행X
                return
        
    # 현재 종이가 같은 숫자 구성 -> 해당 숫자 카운트, 함수 종료
    result[current] += 1
    return

# 초기 종이에 대해 함수 호출 통해 전체 영역 대상으로 함수 실행
divided(0, 0, n)

# 결과 출력
# values() : 딕셔너리에 저장된 모든 값 반환
for i in result.values():
    print(i)