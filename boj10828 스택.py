# 백준 10828 스택
### 파이썬에선 스택구조를 따로 지원하지 않음
### 리스트 활용하여 구현 가능
###'deque' 사용하여 요소의 개수가 많고 push/pop이 자주 이뤄질 때 빠르게 동작 가능
import sys
from collections import deque
n = int(sys.stdin.readline())

stack = deque()

for _ in range(n):
    s = sys.stdin.readline().split()

# push x : 정수 x를 스택에 넣가
    if s[0] == 'push':
        stack.append(s[1])

# pop : 스택에서 가장 위에 있는 정수를 빼고 그 수 출력. 
# 만약 스택에 정수가 없는 경우 -1 출력
    elif s[0] == 'pop':
        if stack:
            print(stack.pop())
        else: 
            print(-1)

# size : 스택에 들어있는 정수의 개수 출력
    elif s[0] == 'size':
        print(stack.len())

# empty : 스택이 비어있으면 1, 아니면 0 출력
    elif s[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

# top : 스택의 가장 위에 있는 정수 출력, 없으면 -1 출력
    elif s[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)