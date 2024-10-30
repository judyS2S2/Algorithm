### 백준 3052. 나머지
# 주어진 수를 42로 나눈 나머지 중 서로 다른 나머지의 개수 세기
import sys
input = sys.stdin.readline

#res = set()
#for _ in range(10):
#    num = int(input())
#    remainder = num % 42
#    res.add(remainder)

#print(len(res))


arr = list(int(input()) for _ in range(10))
# 모듈 0
# 10개의 숫자 배열 -> 42로 나눈 나머지 배열
arr_42 = list(map(lambda x : x % 42, arr))
# 모듈 1
# 42로 나눈 나머지 배열 -> 고유한 숫자 데이터
res = list(set(arr_42))
# 모듈 2
# 고유한 숫자 데이터 -> 개수
print(len(res))