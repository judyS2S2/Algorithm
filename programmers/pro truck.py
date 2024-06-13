from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 시간과 bridge_length와 동일한 길이를 가진 0으로 구성된 bridge 초기화
    answer = 0
    bridge = deque([0] * bridge_length)

    current_weight = 0
    while len(truck_weights)>0:
        answer += 1
        current_weight = current_weight - bridge.popleft()

        # 다리 건너는 트럭 무게 + 대기중인 트럭 <= 감당 무게
        if current_weight + truck_weights[0] <= weight:
            current_weight = current_weight + truck_weights[0]
            bridge.append(truck_weights.pop(0))

        else:
            bridge.append(0)
    answer = answer + bridge_length
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))