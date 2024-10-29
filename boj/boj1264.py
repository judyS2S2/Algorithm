### 백준 1264. 모음의 개수
# 문장에서 모음의 개수 세기 (대소문자 구분 X)
# read() : 파일을 통째로 읽음
# readline() : 줄 단위로 읽어 한줄로 출력
# readlines() : 줄 단위로 읽어 리스트로 만들어준다. + 끝마다 \n
import sys
input = sys.stdin.read

data = input().splitlines()
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

for line in data:
    if line == '#':
        break
    count = sum(1 for char in line if char in vowels)
    print(count)