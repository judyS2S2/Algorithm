### 백준 16113. 시그널
# 시그널을 숫자로 변환하여 출력

import sys
input = sys.stdin.readline

# 시그널 길이 n 입력받기
n = int(input().strip())
# 시그널 데이터 입력받기
signal = input().strip()
# 시그널 5등분 한 열의 길이 m 계산
m = n // 5
# 임시로 시그널의 각 부분을 저장할 문자열
tmp = ''
# 전치하기 전의 시그널 저장할 리스트
d_signal =  []
# 현재 확인 중인 숫자 패턴을 저장할 리스트
check = []

# 숫자들의 패턴 미리 정의
numbers = [
    ['#####', '#...#', '#####'],    # 0
    ['#####'],                      # 1
    ['#.###', '#.#.#', '###.#'],    # 2
    ['#.#.#', '#.#.#', '#####'],    # 3
    ['###..', '..#..', '#####'],    # 4
    ['###.#', '#.#.#', '#.###'],    # 5
    ['#####', '#.#.#', '#.###'],    # 6
    ['#....', '#....', '#####'],    # 7
    ['#####', '#.#.#', '#####'],    # 8
    ['###.#', '#.#.#', '#####']     # 9
]

# 시그널 5등분하여 각 부분 d_signal에 추가
for i, c in enumerate(signal, start = 1):
    tmp += c
    if i % m == 0:
        # '.'을 추가하여 각 행 길이 맞추기
        # 이후 전치된 배열 사용 시, 각 숫자와 공백 구분
        d_signal.append(list(tmp) + ['.'])
        tmp = ''

# 시그널을 세로로 읽기 위해 tranpose
# zip(*) -> 각 행의 요소들을 각각 묶어서 새로운 튜플 생성
d_signal = list(map(list, zip(*d_signal)))

# 해독된 숫자 저장할 문자열
answer = ''

# 전치된 시그널 하나씩 확인
for a in d_signal:
    # 열을 하나의 문자열로 결합
    letters = ''.join(a)

    # 열이 공백이 아닌 경우(모두 '.'이 아닌 경우) check에 추가
    if letters != '.....':
        check.append(letters)
    
    else:
        # 공백을 만나면 check에 저장된 패턴을 숫자 패턴과 비교
        if check:
            # 숫자 패턴 0~9까지 비교
            for idx in range(10):
                # 패턴이 숫자와 일치하면 해당 숫자를 answer에 추가
                if check == numbers[idx]:
                    answer += str(idx)
                    # check 다시 초기화
                    check = []

# 결과 출력
print(answer)