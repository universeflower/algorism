import queue

class Node:#노드 클래스 설정
    def __init__(self, level, weight, profit, bound, include):
        self.level = level  # 노드의 레벨
        self.weight = weight    # 노드의 무게
        self.profit = profit    # 노드의 무게
        self.bound = bound  # 노드의 무게
        self.include = include  # 노드의 포함 여부

    def __lt__(self, other):
        return self.bound < other.bound


def kp(i, profit, weight, node_count):
    global bestset  # 최적해
    global maxp  # 최대 이익
    node_count += 1 # 방문한 노드의 개수 증가

    if weight <= W and profit > maxp:   # 현재 노드의 이익이 최대 이익 초과
        maxp = profit
        bestset = include[:]

    if promising(i, weight, profit):    # 현재 노드가 유망한 노드이면
        include[i + 1] = 1   # 현재 노드의 포함 여부를 1로 설정
        node_count = kp(i + 1, profit + p[i + 1], weight + w[i + 1], node_count)     # 재귀적으로 탐색
        include[i + 1] = 0   # 현재 노드의 포함 여부를 0으로 설정
        node_count = kp(i + 1, profit, weight, node_count)  # 재귀적으로 탐색

    return node_count


def promising(i, weight, profit):
    global maxp #최대이익
    if weight >= W: # 현재 노드의 무게가 가방의 용량을 초과
        return False
    else:
        j = i + 1
        bound = profit  # 경계값 초기화
        totweight = weight  # 총 무게 초기화
        while j < n and totweight + w[j] <= W:  # 다음 노드가 가방의 용량을 초과하지 않음
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if k < n:   # 마지막 노드가 가방의 용량을 초과하지 않음
            bound += (W - totweight) * p[k] / w[k]
        return bound > maxp # 경계값이 최대 이익보다 크면 유망한 노드


def kp_Best_FS():   #최대 이익을 가지는 아이템 집합을 찾는 함수
    global maxProfit
    global bestset
    temp = n * [0]
    v = Node(-1, 0, 0, 0.0, temp)   # 노드 v를 생성
    pq = queue.PriorityQueue()  # 우선순위 큐를 생성
    v.bound = compBound(v)
    pq.put((-v.bound, v))   # v를 우선순위 큐에 넣음
    u = Node(0, 0, 0, 0.0, temp)     # 노드 u를 생성합니다.
    node_count = 1  # 노드의 개수를 1로 설정합니다.
    maxPQSize = 1
    currentPQSize = 1

    while not pq.empty(): # 노드의 개수를 1로 설정합니다.
        v = pq.get()[1]  # 우선순위 큐에서 가장 큰 경계값을 가지는 노드 v를 가져옴
        currentPQSize -= 1  # 우선순위 큐의 크기를 1 감소

        if v.bound > maxProfit:  # v의 경계값이 최대 이익보다 큼
    
            level = v.level + 1     # 왼쪽 자식 노드 u를 생성
            weight = v.weight + w[level]
            profit = v.profit + p[level]
            include = v.include[:]
            u = Node(level, weight, profit, 0.0, include)
            u.include[level] = 1
            if u.weight <= W and u.profit > maxProfit:
                maxProfit = u.profit     # 최대 이익을 u의 이익으로 설정
                bestset = u.include      # 최적의 해를 u의 포함 배열로 설정
            u.bound = compBound(u)   # u의 경계값을 계산
            if u.bound > maxProfit:  # u의 경계값이 최대 이익보다 큼
                pq.put((-u.bound, u))    # u를 우선순위 큐에 넣음
                currentPQSize += 1
                node_count += 1

            u = Node(level, v.weight, v.profit, 0.0, v.include) # 오른쪽 자식 노드 u를 생성
            u.bound = compBound(u)
            if u.bound > maxProfit:  # u의 경계값이 최대 이익보다 크면
                pq.put((-u.bound, u))     # u를 우선순위 큐에 넣음
                currentPQSize += 1
                node_count += 1
                maxPQSize = max(maxPQSize, currentPQSize)   # 우선순위 큐의 크기를 최대값으로 설정

    return node_count, maxPQSize


def compBound(u):   # 이 함수는 u의 경계값을 계산하는 함수
    if u.weight >= W:   # u의 가중치가 W를 초과
        return False
    else:
        j = u.level + 1
        bound = u.profit     # u의 경계값을 u의 이익으로 설정
        totweight = u.weight
        while j < n and totweight + w[j] <= W:  # u의 가중치가 W를 초과하지 않음
            totweight += w[j]
            bound += p[j]    # u의 경계값에 아이템의 이익을 더합
            j += 1
        k = j
        if k < n:
            bound += (W - totweight) * p[k] / w[k]
        return bound


n = 4
W = 7
p = [14, 5, 20, 4]
w = [2, 1, 5, 2]
include = [0] * n
maxProfit = 0
bestset = n * [0]
maxp = 0
node_count = 0
maxPQSize = 0

node_count = kp(-1, 0, 0, node_count)
print("깊이우선검색 방법 논리적 상태 공간 트리의 총 노드 개수:", node_count)
print("최대 이익:", maxp)
print("최적 해:", bestset)


node_count, maxPQSize = kp_Best_FS()
print("최고우선검색 방법 논리적 상태 공간 트리의 총 노드 개수:", node_count)
print("우선순위 큐(PQ)에 있는 데이터의 최대 개수:", maxPQSize)
