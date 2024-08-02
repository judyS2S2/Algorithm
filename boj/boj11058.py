### 백준 11058. 크리보드
# 버튼을 총 N번 눌러서 화면에 출력된 A개수를 최대 출력
import sys
input = sys.stdin.readline
# 버튼 누르는 횟수
n = int(input())
# i번 누르면 i개 A 나오도록 배열 초기화
dp = [i for i in range(n + 1)]

# 6개 이상의 키 입력부터는 복-붙 가능
for i in range(6, n + 1):
    # 선택-복사-붙
    # 선택-복사-붙-붙
    # 선택-복사-붙-붙-붙
    dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

# 결과 출력
print(dp[n])