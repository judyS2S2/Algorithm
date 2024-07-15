### 백준 3568. iSharp
# 조건에 맞게 문자열 출력
import sys
input = sys.stdin.readline
# 입력받아 쉼표 제거하고 공백 기준 분리
tmp = input().replace(',', '').split()
# 기본 변수형 이후의 각 변수 선언 처리
for i in range(1, len(tmp)):
    # 배열 표기 []를 ][로 바꿔서 나중에 처리하기 쉽게 함
    tmp[i] = tmp[i].replace('[]','][').replace(';','')

# 기본 변수형 이후의 각 변수 선언 처리
for i in range(1, len(tmp)):
    # 추가적인 변수형 저장할 변수
    res = ''
    # 변수명 저장할 변수
    alpahbet = ''
    for j in tmp[i]:
        # 문자가 알파벳이면 변수명 추가
        if j.isalpha(): 
            alpahbet += j
        # 알파벳이 아니면 추가적인 변수형에 추가
        else: res += j
    
    # 기본 변수형 + 추가적인 변수형(뒤집어서) + 변수명 + 세미콜론 출력
    print(tmp[0] + res[::-1], alpahbet+';')