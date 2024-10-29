### 백준 1316. 그룹 단어 체커
# 그룹단어의 개수 세기
import sys
input = sys.stdin.readline

# 그룹단어인지 확인하는 함수 정의
def is_group_word(word):
    # 이미 나온 글자 중복없이 기록
    seen = set()
    # 이전 글자
    prev_char = ''

    # 단어들을 글자 단위로 하나씩 순회
    for char in word:
        # 이전 글자랑 다르면
        if char != prev_char:
            # 이미 나온 글자에 있다면
            if char in seen:
                # 그룹단어가 아님
                return False
            # 이미 나온 글자 목록에 현재 글자 추가
            seen.add(char)
            # 이전 글자를 현재 글자로 업데이트
            prev_char = char
    # 그룹단어임을 반환
    return True

# 단어 개수 입력
N = int(input())
# 그룹 단어 개수 초기화
group_word_count = 0
# N개의 단어 순회
for _ in range(N):
    # 단어 양쪽 공백 제거하며 입력
    word = input().strip()
    # 그룹 단어이면
    if is_group_word(word):
        # 개수에 1 더해주기
        group_word_count += 1

# 그룹 단어 개수 출력
print(group_word_count)