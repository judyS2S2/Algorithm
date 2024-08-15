### 백준 1759. 암호 만들기
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들 구하기
import sys
input = sys.stdin.readline

# 암호의 길이, 문자의 종류 수 입력
l, c = map(int, input().split())
# c개의 문자들을 입력받아 정렬
words = sorted(list(map(str, input().split())))
# 결과 저장할 리스트 초기화
answer = []

def dfs(cnt, idx):
    # 현재 선택한 문자 개수가 암호의 길이와 같으면
    if cnt == l:
        # 모음과 자음 개수 초기화
        vo, co = 0, 0

        # 선택한 문자 리스트 순회
        for i in range(l):
            # 현재 문자가 모음인지 확인
            if answer[i] in ['a', 'e', 'i', 'o', 'u']:
                # 모음이면 모음 개수 증가
                vo += 1
            else:
                # 자음이면 자음 개수 증가
                co += 1
        
        # 조건 : 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            # 결과 출력
            print("".join(answer))
        
        return  # 함수 종료
    
    # idx부터 c까지 반복하며 조합 생성
    for i in range(idx, c):
        # 현재 인덱스 문자 선택하여 리스트에 추가
        answer.append(words[i])
        # 다음 단계 위해 재귀 호출
        dfs(cnt + 1, i + 1)
        # 마지막에 추가한 문자 제거하여 백트래킹
        answer.pop()

# 함수 실행
dfs(0, 0)