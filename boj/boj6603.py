### 백준 6603. 로또
# 독일 로또에서 주어진 숫자 집합 s에서 6개의 숫자 선택하는 모든 조합 구하기
import sys
input = sys.stdin.readline

def dfs(depth, idx):
    # 6개가 되면 
    if depth == 6:
        # 현재 조합 출력 및 종료
        print(*out)
        return
    # 현재 인덱스부터 k까지 반복
    for i in range(idx, k):
        # 현재 숫자 조합에 추가
        out.append(s[i])
        # 재귀 호출로 다음 숫자 선택
        dfs(depth + 1, i + 1)
        # 현재 숫자 조합에서 제거하여 백트래킹
        out.pop()

while True:
    # 입력을 리스트로 변환
    array = list(map(int, input().split()))
    # 첫번째 값 k
    k = array[0]
    # k가 0이면 종료 조건
    if k == 0:
        exit()
    # 나머지 값들은 숫자 집합 s
    s = array[1:]
    # 현재 조합 저장할 리스트
    out = []
    # dfs 실행
    dfs(0, 0)
    # 각 테스트 케이스 사이에 빈 줄 출력
    print()