### 프로그래머스 입국심사 lv3
# 이분탐색 - 정렬된 리스트를 범위를 좁혀가며 탐색
def solution(n, times):
    # 가능한 시간의 최솟값과 최댓값을 left, right로 설정
    left = 1
    right = max(times) * n

    # 이분탐색이므로 left가 right 이하인 동안
    while left <= right:
        # 중간값 : (최대+최소)/2 - 반복을 돌면서 새로 계산하므로 초기화 안 해도 됨
        mid = (left + right) // 2
        # 심사한 사람 수 초기화
        people = 0

        for time in times:
            # 주어진 시간 내 심사할 수 있는 사람 수 계산
            people += mid // time

            # 심사한 사람 수가 n 이상이면 종료
            if people >= n:
                break
        
        # n명 초과 심사 -> 시간 많은 것, n명이라도 시간 남을 가능성 고려
        if people >= n:
            # 가능한 시간 저장
            answer = mid
            # 시간 남으면 최대 시간 줄이기
            right = mid - 1
        
        # n명 미만이라면, 시간 부족
        else:
            left = mid + 1
    
    return answer

print(solution(6, [7, 10]))