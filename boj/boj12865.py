### 백준 12865. 평범한 배낭
# 배낭에 넣을 수 있는 물건들의 가치합의 최댓값 출력
import sys
input = sys.stdin.readline

# 물건의 수 n, 최대 무게 k 입력받기
n, k = map(int, input().split())
# 물건 정보 저장할 리스트 초기화, 첫번째 요소 사용X
# 1-based 인덱싱 -> 물건번호와 인덱스 일치 위함
# d[i][j] : i (물건 번호), j (배낭 현재 무게)
thing = [[0, 0]]
# DP 테이블 초기화, (n+1)x(k+1) 크기의 2차원 리스트
d = [[0] * (k+1) for _ in range(n+1)]

# 각 물건의 무게와 가치 입력받기
for i in range(n):
    thing.append(list(map(int, input().split())))

# 1번부터 n번 물건까지 순회
for i in range(1, n+1):
    # 1부터 최대 무게 k까지 순회
    for j in range(1, k+1):
        # 현재 물건의 무게
        w = thing[i][0]
        # 현재 물건의 가치
        v = thing[i][1]

        # 현재 배낭에 허용된 무게 j가 현재 고려중인 물건 무게 w보다 작다면
        if j < w:
            # 물건 넣지 않음
            d[i][j] = d[i-1][j]
        else:
            # 물건 넣지 않는 경우와 넣는 경우 중 큰 값 선택
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

# 최종적으로 n개의 물건과 최대 무게 k에서의 최대 가치 출력
print(d[n][k])