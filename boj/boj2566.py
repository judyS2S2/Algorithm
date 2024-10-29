### 백준 2566. 최댓값
# 주어진 수 중 최댓값을 찾고, 해당 위치 출력
import sys
input = sys.stdin.readline

numbers = [list(map(int, input().rstrip().split())) for _ in range(9)]
# print(numbers)

max_value = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if numbers[i][j] > max_value:
            max_value = numbers[i][j]
            max_row, max_col = i + 1, j + 1

print(max_value)
print(max_row, max_col)