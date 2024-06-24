### 백준 11399. ATM
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값
import sys
input = sys.stdin.readline

# 사람의 수 n 입력
n = int(input().strip())
# 각 사람이 돈을 인출하는데 걸리는 시간
people = list(map(int, input().split()))

# 오름차순 정렬
people.sort()

# 결과값 초기화
result = 0

# 누적합 변수 초기화
current = 0

# 누적합 계산하여 결과값 갱신
for time in people:
    current += time
    result += current

print(result)