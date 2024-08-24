### 프로그래머스 정수 삼각형
# 경로에서 거쳐간 숫자들의 합이 가장 큰 경우 구하기

# 삼각형 배열이 입력으로 들어옴
def solution(triangle):
    # 두번째 줄부터 마지막 줄까지 반복(첫 줄은 계산할 필요 X)
    for i in range(1, len(triangle)):
        # 각 줄의 모든 요소 순회
        for j in range(len(triangle[i])):
            # 현재 요소가 줄의 첫번째 요소이면
            if j == 0:
                # 바로 위 요소만 더함 (첫번째 요소)
                triangle[i][j] += triangle[i - 1][0]
            # 현재 요소가 줄의 마지막 요소이면
            elif j == len(triangle[i] - 1):
                # 바로 위 요소만 더함 (마지막 요소)
                triangle[i][j] += triangle[i - 1][-1]
            else: # 그 외 경우
                # 위의 두 요소 중 큰 값 더하기
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    # 마지막 줄에서 가장 큰 값 반환
    return max(triangle[-1])