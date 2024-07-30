### 백준 11727. 2xn 타일링 2
# 2xn 크기의 직사각형 채우는 방법의 수를 10,007로 나눈 나머치 출력
import sys
input = sys.stdin.readline

# 직사각형 가로 n 입력
n = int(input())
# 방법의 수 저장할 리스트 정의 및 초기화
rectangular = [0] * 1001
# 2*1 크기 직사각형 채우는 방법의 수 = 1
rectangular[1] = 1

# n이 2 이상인 경우 정의
if n >= 2:
    # 2*2 크기일 때 3가지
    rectangular[2] = 3
    # 2*3부터 n까지 dp 통해 직사각형 채우는 방법의 수 정의
    for i in range(3, n+1):
        # 점화식 정의
        rectangular[i] = (rectangular[i-2] * 2) + rectangular[i-1]

# 결과 출력
print(rectangular[n] % 10007)