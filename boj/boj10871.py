### 백준 10871. X보다 작은 수
# 주어진 수열에서 X보다 작은 수 출력
import sys
input = sys.stdin.readline

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i, end=' ')