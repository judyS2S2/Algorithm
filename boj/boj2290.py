### 백준 2290. LCD Test
# 숫자로 구성된 문자열을 주어진 칸 수에 맞게 출력
import sys
input = sys.stdin.readline

# 입력받기
s, n = map(int, input().split())

def print_lcd(s, n):
    # 각 숫자가 사용하는 세그먼트 리스트
    digits = [
        [1, 2, 3, 5, 6, 7],       # 0
        [3, 6],                   # 1
        [1, 3, 4, 5, 7],          # 2
        [1, 3, 4, 6, 7],          # 3
        [2, 3, 4, 6],             # 4
        [1, 2, 4, 6, 7],          # 5
        [1, 2, 4, 5, 6, 7],       # 6
        [1, 3, 6],                # 7
        [1, 2, 3, 4, 5, 6, 7],    # 8
        [1, 2, 3, 4, 6, 7]        # 9
    ]

    # 숫자를 문자열로 변환
    n_str = str(n)
    # LCD 숫자의 높이 (세로)
    height = 2 * s + 3
    # LCD 숫자의 너비 (가로)
    width = s + 2

    # 전체 출력할 행렬을 공백으로 초기화
    lcd_output = [[' ' for _ in range(width * len(n_str) + (len(n_str) - 1))] for _ in range(height)]

    # 각 자리 숫자에 대해 반복
    for i, digit in enumerate(n_str):
        # 현재 숫자가 사용하는 세그먼트 리스트
        segs = digits[int(digit)]
        # 현재 숫자의 시작 위치 (가로 오프셋 -> 공백 포함)
        offset = i * (s + 3)
        
        # 각 세그먼트를 해당 위치에 그리기
        if 1 in segs:
            # 세그먼트 1은 상단 가로선, 가로 방향으로 s 길이만큼 '-' 그리기
            for j in range(1, s + 1):
                # 세그먼트 1
                lcd_output[0][offset + j] = '-'
        if 2 in segs:
            # 세그먼트 2는 좌상단 세로선, 세로 방향으로 s 길이만큼 '|' 그리기
            for j in range(1, s + 1):
                # 세그먼트 2
                lcd_output[j][offset] = '|'
        if 3 in segs:
            # 세그먼트 3은 우상단 세로선, 세로 방향으로 s 길이만큼, 오른쪽 위치하도록
            # offset + s + 1로 범위 설정
            for j in range(1, s + 1):
                # 세그먼트 3
                lcd_output[j][offset + s + 1] = '|'
        if 4 in segs:
            # 세그먼트 4는 중간 가로선, s+1번째 행에 위치하고 offset+1부터 offset+s까지 '-'로 채우기
            # j가 해당 범위 반복
            for j in range(1, s + 1):
                # 세그먼트 4
                lcd_output[s + 1][offset + j] = '-'
        if 5 in segs:
            # 세그먼트 5는 좌하단 세로선, s+2번째 행부터 2s+2번째 행까지 '|'로 채우기
            for j in range(s + 2, 2 * s + 2):
                # 세그먼트 5
                lcd_output[j][offset] = '|'
        if 6 in segs:
            # 세그먼트 6은 우하단 세로선, s+2번째 행부터 2s+2번째, 오른쪽으로 '|' 채우기
            # 오른쪽 -> offset + s + 1
            for j in range(s + 2, 2 * s + 2):
                # 세그먼트 6
                lcd_output[j][offset + s + 1] = '|'
        if 7 in segs:
            # 세그먼트 7은 하단 가로선, 2s+2번째 행
            for j in range(1, s + 1):
                # 세그먼트 7
                lcd_output[2 * s + 2][offset + j] = '-'
		# 행렬의 각 행을 하나의 문자열로 만들어 출력
    for row in lcd_output:
        print(''.join(row))

# 출력하기
print_lcd(s, n)