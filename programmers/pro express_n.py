### 프로그래머스 N으로 표현
# N의 최소 사용 횟수 출력
def solution(N, number):
    # 초기값 -1, 목표 숫자를 찾지 못할 경우 반환
    answer = -1
    # N을 i번 사용해서 만들 수 있는 숫자들을 저장하는 집합을 각 자리마다 저장 (0~8, 총 9개)
    dp = [set() for i in range(9)]
    
    # 1번부터 8번까지 N을 사용하는 경우
    for i in range(1, 9):
        # N을 i번 사용한 숫자를 추가 (예: 5, 55, 555 등)
        dp[i].add(int(str(N)*i))
        
        # j는 N을 j번 사용한 경우의 집합을 탐색
        for j in range(i):
            # j번 사용한 숫자들 중 하나를 가져옴
            for first in dp[j]:
                # (i-j)번 사용한 숫자들 중 하나를 가져옴
                for second in dp[i-j]:
                    # 두 숫자를 더한 결과 추가
                    dp[i].add(first + second)
                    # 두 숫자를 뺀 결과 추가
                    dp[i].add(first - second)
                    # 두 숫자를 반대로 뺀 결과 추가
                    dp[i].add(second - first)
                    # 두 숫자를 곱한 결과 추가
                    dp[i].add(first * second)
                    
                    # 나눗셈은 분모가 0이 아닌 경우에만 수행
                    if second != 0:
                        # 두 숫자를 나눈 결과 추가
                        dp[i].add(first // second)
                    # 나눗셈은 분모가 0이 아닌 경우에만 수행
                    if first != 0:
                        # 두 숫자를 반대로 나눈 결과 추가
                        dp[i].add(second // first)
        
        # 만약 dp[i]에 목표 숫자가 있으면
        if number in dp[i]:
            # 그때의 i값(= N 사용 횟수)을 답으로 저장하고
            answer = i
            # 반복 종료
            break
    
    # 정답 반환
    return answer