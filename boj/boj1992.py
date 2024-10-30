### 백준 1992. 쿼드트리
# 압축결과에 맞게 출력 결과 반환
import sys
input = sys.stdin.readline

# 한 변의 길이
N = int(input())
# 영상 -> 2차원 배열
video = [list(map(int, input().strip())) for _ in range(N)]

# 함수 정의 -> 왼쪽 위 좌표와 오른쪽 아래 좌표 통해 해결
# i : 행, j : 열
def func(li, lj, ri, rj):
    # 종료 조건 -> 1칸일 때 / 같은 결과일 때
    if ri - li == 1:
        return str(video[li][lj])
    
    first_value = video[li][lj]
    is_consistent = True
    for i in range(li, ri):
        for j in range(lj, rj):
            if first_value != video[i][j]:
                is_consistent = False
                break
            if not is_consistent:
                break
    
    if is_consistent:
        return str(first_value)
    
    # 재귀 호출 -> 자르기 위해 중간값 도출
    mi = (li + ri) // 2
    mj = (lj + rj) // 2

    # 4면 호출
    rec1 = func(li, lj, mi, mj)
    rec2 = func(li, mj, mi, rj)
    rec3 = func(mi, lj, ri, mj)
    rec4 = func(mi, mj, ri, rj)

    # 데이터 통합
    return f"({rec1}{rec2}{rec3}{rec4})"

# 출력값
res = func(0, 0, N, N)
print(res)