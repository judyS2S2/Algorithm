### 백준 1931. 회의실 배정
# 최대 사용할 수 있는 회의의 최대 개수 구하기
import sys
input = sys.stdin.readline
# 회의 개수 입력
n = int(input())
# 회의 시간 저장할 리스트 초기화
timeline = []
# n줄 동안 회의 시간 입력 받기 + 리스트에 추가
for _ in range(n):
    start, end = map(int, input().split())
    timeline.append((start, end))

# 종료 시간 기준으로 오름차순 정렬
timeline.sort(key = lambda x : (x[1], x[0]))

# 첫번째 회의 필수적 선택
end = timeline[0][1]

# 결과값 초기화
count = 1

# 종료 시간 < 시작 시간 -> 현재 회의 종료 시간으로 갱신
for i in range(1, n):
    if timeline[i][0] >= end:
        end = timeline[i][1]
        # 결과값 + 1
        count += 1

# 결과값 출력
print(count)