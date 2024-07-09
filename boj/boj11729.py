### 백준 11729. 하노이 탑 이동 순서
# 원판 옮긴 총 횟수와 이동 과정 출력
import sys
input = sys.stdin.readline

# 원판의 개수 n 입력
n = int(input())

# 하노이 탑 재귀 함수
def hanoi(n, start, mid, end):
    # base case : 원판이 1개인 경우
    if n == 1:
        # 1개의 원판을 출발지에서 목적지로 이동
        print(start, end)
        return
    
    else:
        # 제일 마지막 원판 제외한 나머지를 가운데로 이동
        hanoi(n-1, start, end, mid)
        # 마지막 원판을 세번째로 이동
        print(start, end)
        # 가운데 있던 원판들을 세번째로 이동
        hanoi(n-1, mid, start, end)
        return

# 이동 횟수는 2^n - 1
sum = 2 ** n - 1
print(sum)

# 하노이 함수 호출
hanoi(n, 1, 2, 3)