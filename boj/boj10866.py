### 백준 10866. 덱
# 덱 메소드 함수 구현
from collections import deque
import sys
input = sys.stdin.readline

# 입력값
# 명령어 개수
N = int(input())
# 명령어
orders = [input().split() for _ in range(N)]
# 저장 -> 덱
q = deque()
# 각 기능별 함수 정의
# push_front (appendleft())
def push_front(n):
    q.appendleft(n)
# push_back (append())
def push_back(n):
    q.append(n)
# pop_front (popleft())
def pop_front():
    if q:
        return q.popleft()
    else:
        return -1
# pop_back (pop())
def pop_back():
    if q:
        return q.pop()
    else:
        return -1
# size
def size():
    return len(q)
# empty
def empty():
    if q:
        return 0
    else:
        return 1
# front
def front():
    if q:
        return q[0]
    else:
        return -1
# back
def back():
    if q:
        return q[-1]
    else:
        return -1
# 함수 호출 및 실행
for order in orders:
    if order[0] == 'push_front':
        push_front(int(order[1]))
    
    elif order[0] == 'push_back':
        push_back(int(order[1]))

    elif order[0] == 'pop_front':
        print(pop_front())

    elif order[0] == 'pop_back':
        print(pop_back())

    elif order[0] == 'size':
        print(size())

    elif order[0] == 'empty':
        print(empty())
    
    elif order[0] == 'front':
        print(front())
    
    elif order[0] == 'back':
        print(back())