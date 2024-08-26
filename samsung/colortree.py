### 삼성기출. 색깔 트리
# 노드 추가/색깔 변경/색깔 조회/점수 조회 순으로 진행하며 알맞은 답 출력
import sys
input = sys.stdin.readline

# ID의 최댓값
max_id = 100005
# 트리의 최대 깊이
max_depth = 105
# 색깔 최대 개수 (빨 : 1, 주 : 2, 노 : 3, 초 : 4, 파 : 5)
color_max = 5

# 노드ID, 색깔, 마지막 업데이트 시간, 최대 깊이, 부모ID, 자식 저장
class Node:
    def __init__(self):
        # 노드 고유 번호
        self.id = 0
        # 노드 색깔 (1-5)
        self.color = 0
        # 노드가 마지막으로 업데이트 된 시간 (마지막 노드 추가/색깔 변경 시점)
        self.lastUpdate = 0
        # 노드가 가질 수 있는 최대 깊이
        self.maxDepth = 0
        # 부모노드 id 저장
        self.parentId = 0
        # 자식노드 id들 목록 저장
        self.childIds = []

# 점수 계산 위한 클래스 생성, 각 색깔의 개수 저장 (1-5)
class ColorCount:
    def __init__(self):
        # 각 색깔의 개수 저장 (1-5)
        self.cnt = [0] * (color_max + 1)

    # 두 ColorCount 객체 더해서 색깔 개수 합침
    def __add__(self, obj):
        # 결과 저장할 새 객체 생성
        res = ColorCount()
        for i in range(1, color_max + 1):
            # 각 색깔 개수 더하기
            res.cnt[i] = self.cnt[i] + obj.cnt[i]
        # 합친 결과 반환
        return res

    # 서로 다른 색의 개수 계산 및 개수의 제곱 반환
    def score(self):
        # 색깔 개수 계산한 값 저장
        result = 0
        for i in range(1, color_max + 1):
            # 색깔 있으면 1 더하기 아니면 0
            result += 1 if self.cnt[i] else 0
        # 색깔의 개수 제곱 반환
        return result ** 2

# 모든 노드 저장할 리스트 생성, 각 리스트 자리에 Node 객체 들어감 
nodes = [Node() for _ in range(max_id)]
# 루트 노드 여부 저장하는 리스트
isRoot = [False] * max_id

# 해당 노드가 자식노드를 가질 수 있는지 확인
# 해당 과정에서는 루트까지 조상들을 각각 탐색하며 maxDepth 확인
def canMakeChild(curr, needDepth):
    # 노드 X면 True
    if curr.id == 0:
        return True
    # 노드 최대 깊이보다 더 깊으면 False
    if curr.maxDepth <= needDepth:
        return False
    # 부모 노드로 올라가면서 깊이 확인
    return canMakeChild(nodes[curr.parentId], needDepth + 1)

# curr 노드의 색깔 정보와 해당 색깔이 설정된 시간 return
# root에 도달할때까지 부모를 거슬러 올라가며 lastUpdate시간을 이용하여 현재 노드가 가져야하는 색깔을 계산
def getColor(curr):
    # 루트 노드까지 가면 0 반환
    if curr.id == 0:
        return 0, 0
    # 부모 노드 색 정보 가져오기
    info = getColor(nodes[curr.parentId])
    # 부모 노드 색이 더 최신이면 부모 색 반환
    if info[1] > curr.lastUpdate:
        return info
    else:
        # 아니면 현재 노드 색 반환
        return curr.color, curr.lastUpdate

# 트리 점수 계산
def getBeauty(curr, color, lastUpdate):
    # 현재 노드가 더 최근에 업데이트됐으면 정보 갱신
    if lastUpdate < curr.lastUpdate:
        lastUpdate = curr.lastUpdate
        color = curr.color
    # 점수와 색깔 개수 정보를 저장할 변수 생성
    result = [0, ColorCount()]
    # 현재 노드 색깔 개수를 1로 설정
    result[1].cnt[color] = 1
    # 자식 노드들에 대해 재귀적으로 점수 계산
    for childId in curr.childIds:
        child = nodes[childId]
        # 자식 노드에서 점수와 색깔 개수 가져오기
        subResult = getBeauty(child, color, lastUpdate)
        # 색깔 개수 더하기
        result[1] = result[1] + subResult[1]
        # 점수 더하기
        result[0] += subResult[0]
    # 마지막으로 자신의 점수 더하기
    result[0] += result[1].score()
    # 최종 점수 반환
    return result

if __name__ == "__main__":
    # 명령의 수 입력받기
    Q = int(input())
    # 각 명령을 하나씩 처리
    for i in range(1, Q + 1):
        # 명령의 내용 입력받기
        query = list(map(int, input().split()))
        T = query[0]
        # 노드 추가 명령
        if T == 100:
            mId, pId, color, maxDepth = query[1:]
            # 부모의 Id가 -1인 경우 root노드
            if pId == -1:
                isRoot[mId] = True
            # 노드 추가할 수 있는지 확인
            if isRoot[mId] or canMakeChild(nodes[pId], 1):
                # node 정보를 기입
                nodes[mId].id = mId # 노드 ID 설정
                nodes[mId].color = color # 노드 색깔 설정
                nodes[mId].maxDepth = maxDepth # 노드 최대 깊이 설정
                nodes[mId].parentId = 0 if isRoot[mId] else pId # 부모 ID 설정
                # 업데이트 시간을 현재 시간으로 설정
                nodes[mId].lastUpdate = i

                # 루트가 아니면 부모 노드에 자식 노드로 추가
                if not isRoot[mId]:
                    nodes[pId].childIds.append(mId)
        
        # 색깔 변경 명령
        elif T == 200:
            mId, color = query[1:]
            # 노드 색깔 변경
            nodes[mId].color = color
            # 업데이트 시간을 현재 시간으로 설정
            nodes[mId].lastUpdate = i
        
        # 색깔 조회 명령
        elif T == 300:
            mId = query[1]
            # 노드 색깔 출력
            print(getColor(nodes[mId])[0])
        
        # 점수 조회 명령
        elif T == 400:
            beauty = 0
            # 모든 루트 노드에 대해 점수 계산
            for i in range(1, max_id):
                if isRoot[i]:
                    beauty += getBeauty(nodes[i], nodes[i].color, nodes[i].lastUpdate)[0]
            # 최종 점수 출력
            print(beauty)