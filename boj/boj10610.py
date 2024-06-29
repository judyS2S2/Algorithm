### 백준 10610. 30
# n으로 만들 수 있는 30의 배수 중 가장 큰 수 출력
import sys
input = sys.stdin.readline
# n 입력 및 입력 받고 줄바꿈 문자 제거
n = list(input().strip())
# 입력값이 '0'인 경우 처리
if n == ['0']:
    print(-1)

else:
    # 내림차순 정렬
    n.sort(reverse = True)

    # 정수로 변환하여 각 자리 수 합 계산
    sum = sum(int(i) for i in n)

    # 3의 배수 조건과 '0' 포함(10의 배수 조건) 확인
    if (sum % 3) != 0 or '0' not in n:
        print(-1)

    else:
        # 가장 큰 숫자 출력
        print(''.join(n))