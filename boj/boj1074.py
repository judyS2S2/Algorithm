### 백준 1074. Z
# r행 c열을 몇 번째로 방문했는지 출력
import sys
input = sys.stdin.readline

# n, r, c 입력
n, r, c = map(int, input().split())

# 재귀 함수 정의
def z(n, r, c, q):
    # 기본 조건 : n이 0이 되면 현재까지의 순서 q를 return
    if n == 0:
        return (q)
    
    # 한 변의 절반 길이
    half = 2 ** (n-1)

    # 1사분면 혹은 2사분면인 경우
    if r < half:
        # 1사분면
        if c < half:
            quad = 1

        # 2사분면
        else:
            ### 사분면 결정 후, 사분면 내의 상대적 좌표 계산 -> 재귀 사용
            # c를 절반만큼 줄여서 새로운 좌표 설정
            c -= half
            quad = 2
    
    # 3사분면 혹은 4사분면인 경우
    else:
        # 3사분면
        if c < half:
            # r을 절반만큼 줄여서 새로운 좌표 설정
            r -= half
            quad = 3
        
        # 4사분면
        else:
            # r을 절반만큼 줄여서 새로운 좌표 설정
            r -= half
            # c를 절반만큼 줄여서 새로운 좌표 설정
            c -= half
            quad = 4

    # 현재 사분면까지의 순서를 계산하여 더해주기
    q += (quad - 1) * (half ** 2)
    # n을 줄이고, 새로운 r, c로 재귀 호출
    return z((n - 1), r, c, q)

# 결과 출력
print(z(n, r, c, 0))