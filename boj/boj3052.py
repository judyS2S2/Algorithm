### 백준 3052. 나머지
# 주어진 수를 42로 나눈 나머지 중 서로 다른 나머지의 개수 세기
import sys
input = sys.stdin.readline

res = set()
for _ in range(10):
    num = int(input())
    remainder = num % 42
    res.add(remainder)

print(len(res))