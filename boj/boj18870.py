### 백준 18870. 좌표 압축
# 좌표 압축 결과 도출
import sys
input = sys.stdin.readline
# 좌표의 개수 입력
n = int(input())
# n개의 좌표 입력받아 리스트로 변환
nums = list(map(int, input().split()))
# 좌표에서 중복 제거 후 정렬하여 리스트 생성
nums2 = sorted(list(set(nums)))
# 정렬된 각 값을 인덱스로 매핑하는 딕셔너리 생성
dic = {nums2[i] : i for i in range(len(nums2))}
# 원래 좌표 리스트를 순회하며
for i in nums:
    # 각 좌표를 압축된 값으로 변환하여 출력
    print(dic[i], end = ' ')