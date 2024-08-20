### 백준 2616. 소형기관차
# 3대를 이용하여 최대로 운송할 수 있는 손님 수 구하기
import sys
input = sys.stdin.readline

# 기관차가 끌고 가던 객차의 수 입력
n = int(input())
# 객차에 타고 있는 손님의 수 차례대로 입력
people = list(map(int, input().split()))
# 기관차가 최대로 끌 수 있는 객차 수 입력
limit = int(input())
# 초기 limit 길이의 연속구간에 대한 손님 수의 합 계산
val = sum(people[:limit])
# limit 길이의 연속 구간 손님 수 합을 저장할 리스트 초기화
people_sum = [val]

# 각 연속 구간의 손님 수 합 계산
for i in range(n-limit):
    # 이전 구간에서 새로운 객차 추가, 기존 객차 제거하여 합 업데이트
    val += people[i+limit] - people[i]
    # 업데이트된 합 리스트에 추가
    people_sum.append(val)

# dp 초기화: (n+1)*4 크기
dp = [[0] * (4) for _ in range(n+1)]

# dp 테이블 채워나가면서 최적 손님 수 계산
for i in range(1, n+1):
    for j in range(3):
        # 현재 위치에서 j번째 소형 기관차가 맡는 최대 손님 수 게산
        dp[i][j] = dp[i-1][j]
        # i 위치에서 limit 길이의 구간 사용 경우 고려
        if i >= limit:
            dp[i][j] = max(dp[i][j], dp[i-limit][j+1] + people_sum[i-limit])
# dp 테이블의 마지막 값, 3대의 소형 기관차를 사용했을 때의 최대 손님 수 계산
print(dp[-1][0])