### 백준 2738. 행렬 덧셈
# N*M 크기의 두 행렬 주어졌을 때, 두 행렬 더하는 프로그램
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
matrix_A = [list(map(int, input().split())) for _ in range(N)]
matrix_B = [list(map(int, input().split())) for _ in range(N)]

result_Matrix = [[matrix_A[i][j] + matrix_B[i][j] for j in range(M)] for i in range(N)]

for row in result_Matrix:
    print(" ".join(map(str, row)))