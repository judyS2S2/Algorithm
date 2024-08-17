### 백준 2661. 좋은 수열
# 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력
import sys
input = sys.stdin.readline

# 수열의 길이 입력
n = int(input())
# 좋은 수열 저장할 리스트
arr = []

# 현재 수열 arr의 마지막 부분이 '나쁜 수열'인지 검사
def check():
    # 수열 길이의 절반까지 탐색
    for i in range(1, len(arr) // 2 + 1):
        # 마지막 i 길이의 부분 수열이 그 앞의 i 길이 부분 수열과 같은지 확인
        if arr[-i:] == arr[-i * 2 : -i]:
            # 나쁜 수열이면 False
            return False
    # 좋은 수열이면 True
    return True

def back_tracking(depth):
    # 현재 수열이 나쁜 수열이면 진행 X, 되돌아감
    if not check():
        return False
    
    # 수열의 길이 n이면
    if depth == n:
        # 수열 출력 (공백없이)
        print(*arr, sep='')
        # 원하는 수열 찾았으므로 True
        return True
    
    # 수열에 1, 2, 3 중 하나 추가하면서
    for next in [1, 2, 3]:
        # 수열에 숫자 추가
        arr.append(next)
        # 재귀 호출하여 다음 숫자 추가하여 탐색
        if back_tracking(depth + 1):
            # 좋은 수열 찾았으면 더 이상 탐색하지 않고 종료
            return True
        # 마지막에 추가한 숫자 제거하고 다음 경우 탐색
        arr.pop()

# 초기 깊이 0에서부터 백트래킹 시작
back_tracking(0)