### 백준 8911. 거북이
# 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형 넓이 구하기
# F : 한 눈금 앞으로
# B : 한 눈금 뒤로
# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전
import sys
input = sys.stdin.readline

# 테스트케이스 개수 입력
t = int(input())
# 각 테스트 케이스 명령어 입력
field = [input() for _ in range(t)]

# 북서남동 방향 설정
# 행렬에서의 방향과 다름, 해당 문제는 좌표계에서의 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for test in field:
    # 초기 방향을 북쪽(0)으로 설정
    direction = 0   # 북 : 0, 서 : 1, 남 : 2, 동 : 3
    # 초기 좌표와 영역의 최소, 최댓값 설정
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    # 초기 위치 (0, 0) 설정
    x, y = 0, 0

    for i in test:
        if i == "F":
            # 현재 방향으로 한 칸 전진
            x += dx[direction]
            y += dy[direction]

        elif i == "B":
            # 현재 방향으로 한 칸 후진
            x -= dx[direction]
            y -= dy[direction]

        elif i == "L":
            # 동->북 왼쪽 전환 시
            if direction == 3:
                direction = 0

            else:
                # 나머지 경우, 왼쪽 전환 시, 방향 증가
                direction += 1

        elif i == "R":
            # 북->동 오른쪽 전환 시
            if direction == 0:
                direction = 3
            else:
                # 나머지 경우, 오른쪽 전환 시, 방향 감소
                direction -= 1
        
        # 영역 구하기 위해 x, y의 최대, 최솟값 저장
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

# 영역 구하기 (최대 x, y와 최소 x, y의 차이로 직사각형의 넓이 계산)
# 음수값 방지 위해 절댓값 처리
print(abs(max_x - min_x) * abs(max_y - min_y))