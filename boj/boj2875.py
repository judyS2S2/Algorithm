### 백준 2875. 대회 or 인턴
# 대회에 나가기 위해 만들 수 있는 최대 팀 개수 구하기
import sys
input = sys.stdin.readline
# 여학생, 남학생, 인턴 인원 수 입력
n, m, k = map(int, input().split())

# 결과값 초기화
count = 0

# 여학생 2명, 남학생 1명 필요, 인턴 제외하고도 3명 이상일 때
while n >= 2 and m >= 1 and n + m >= k + 3:
    # 여학생 2명씩 제외
    n -= 2
    # 남학생 1명씩 제외
    m -= 1
    # 팀 개수 1씩 증가
    count += 1

# 팀 개수 출력
print(count)