### 백준 10845. 큐
# 큐를 이용한 기능 구현
from collections import deque
import sys
input = sys.stdin.readline

# 입력값
# 명령어 개수
N = int(input())
# 명령어 입력
orders = [input().split() for _ in range(N)]
# 저장 -> 덱
queue = deque()

# 각 기능별 함수 정의
# push
def push(n):
    queue.append(n)
# pop
def pop():
    if queue:
        return queue.popleft()
    else:
        return -1
# size
def size():
    return len(queue)
# empty
def empty():
    if queue:
        return 0
    else:
        return 1
# front
def front():
    if queue:
        return queue[0]
    else:
        return -1
# back
def back():
    if queue:
        return queue[-1]
    else:
        return -1
    
# 함수 호출 및 실행
for order in orders:
    if order[0] == 'push':
        push(int(order[1]))
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())