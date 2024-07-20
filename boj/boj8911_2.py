### 백준 8911. 거북이
# 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형 넓이 구하기
# F : 한 눈금 앞으로
# B : 한 눈금 뒤로
# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전
import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스의 개수 입력
field = [input().strip() for _ in range(t)]  # 각 테스트 케이스의 명령어 입력

# 북서남동 방향 정의 (dx, dy 배열로 이동 방향 설정)
# 행렬에서의 방향과 다름, 해당 문제는 좌표계에서의 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for test in field:
    direction = 0   # 초기 방향을 북쪽(0)으로 설정
    # 북(0), 서(1), 남(2), 동(3)
    min_x, min_y, max_x, max_y = 0, 0, 0, 0  # 초기 좌표와 영역의 최소, 최대값 설정
    x, y = 0, 0  # 초기 위치 (0, 0) 설정

    for i in test:
        if i == "F":
            x += dx[direction]  # 현재 방향으로 한 칸 전진
            y += dy[direction]

        elif i == "B":
            x -= dx[direction]  # 현재 방향으로 한 칸 후진
            y -= dy[direction]

        elif i == "L":
            # 북->서, 서->남, 남->동의 경우 방향 증가
            # 동->북의 경우 왼쪽 방향 전환 시, 감소하므로 모듈 계산
            # % 4로 0~3 사이 값 유지
            direction = (direction + 1) % 4  # 왼쪽으로 90도 회전 (북->서->남->동 순으로 증가)

        elif i == "R":
            # 동->남, 남->서, 서->북의 경우 방향 감소 -> 모듈 계산
            # 북->동의 경우 오른쪽 방향 전환 시, 증가하므로 4 더해주기
            direction = (direction - 1) % 4  # 오른쪽으로 90도 회전 (북->동->남->서 순으로 감소)
            # 북->동의 경우, direction = -1
            if direction < 0:
                direction += 4  # 음수일 경우 4를 더해 양수로 변환

        
        # 영역 구하기 위해 x, y의 최대, 최솟값 저장
        min_x, min_y = min(min_x, x), min(min_y, y)
        max_x, max_y = max(max_x, x), max(max_y, y)

    # 영역 구하기 (최대 x, y와 최소 x, y의 차이로 직사각형의 넓이 계산)
    # 음수값 방지 위해 절댓값 처리
    print(abs(max_x - min_x) * abs(max_y - min_y))