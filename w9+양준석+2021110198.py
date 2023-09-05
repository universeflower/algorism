import heapq
import sys

def dijkstra(start):
    # 초기 배열 설정(sys.maxsize 가장큰값=무한대)
    dis = {node: sys.maxsize for node in graph}
    # 시작 노드의 거리는 0으로 설정
    dis[start] = 0
    queue = []
    # 시작 노드부터 탐색 시작 하기 위해
    heapq.heappush(queue, (dis[start], start))
    # 최단 경로를 저장
    path = {start: [start]}

    while queue:
        # 가장 낮은 거리를 가진 노드와 거리를 추출
        cur_dis, node = heapq.heappop(queue)
        # 현재 거리와 노드를 거친 거리를 비교
        if dis[node] < cur_dis:
            continue

        # 대상인 노드에서 인접한 노드와 거리를 순회
        for adj_node, distance in graph[node].items():
            # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함
            fin_dis = cur_dis + distance
            # 배열의 저장된 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경
            if  fin_dis < dis[adj_node]:
                # 배열에 저장된 거리보다 가중치가 더 작으므로 변경
                dis[adj_node] =  fin_dis
                # 최단 경로 업데이트
                path[adj_node] = path[node] + [adj_node]
                # 다음 인접 거리를 계산 하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)
                heapq.heappush(queue, ( fin_dis, adj_node))

    return dis, path

graph = {
    'A': {'B': 7, 'C': 4,'D':6,'E':1},
    'B':{},
    'C': {'B': 2, 'D': 5},
   'D': {'B': 3},
    'E': {'D': 1},
}

dis, path = dijkstra('A')
for node, distance in dis.items():
    print("최단 경로: ", path[node], ", 최단 거리: ", distance)
