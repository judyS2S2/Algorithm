### 백준 9012. 괄호
# 괄호 짝 맞는지 판별 - 스택
import sys
input = sys.stdin.readline

# 입력값
T = int(input())
data = [input().strip() for _ in range(T)]

# 괄호 쌍 맞는지 함수 정의
def is_vpn(s):
    # 스택에 저장
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

for s in data:
    print(is_vpn(s))