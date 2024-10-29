### 백준 2562. 최댓값
# 주어진 수의 최댓값과 위치 출력
import sys
input = sys.stdin.readline

nums = []
for i in range(9):
    num = int(input())
    nums.append(num)

res = max(nums)
index = nums.index(res)
print(res)
print(index + 1)