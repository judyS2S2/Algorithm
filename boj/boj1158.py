import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

people = deque()
# people에 n명 삽입
for i in range(1, n+1):
    people.append(i)

# 결과값 저장할 빈 리스트 생성
result = []

# people이 있을 때까지, 제거된 사람이 n명이 될 때까지
while people:
    # k-1까지 범위 설정으로, k-1개씩 pop으로 빼서 뒤에 추가
    for _ in range(k-1):
        people.append(people.popleft())
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))