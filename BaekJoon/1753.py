from heapq import *
from sys import stdin


def dijkstra(start):
    distance = [float('inf')] * (V + 1)
    distance[start[1]] = 0
    # edges: [(가중치, 도착 정점), ...] 형태의 우선 순위 큐(heap)
    edges = []
    heappush(edges, start)
    
    while edges:
        weight, node = heappop(edges)

        if distance[node] < weight:
            continue

        for next_weight, next_node in graph[node]:
            next_weight += weight
            if distance[next_node] > next_weight:
                distance[next_node] = next_weight
                heappush(edges, (next_weight, next_node))
    
    return distance


# V: 정점의 수, E: 간선의 수
V, E = map(int, input().split())
# K: 시작 정점
K = int(input())
# graph: {출발 정점: [(가중치, 도착 정점), ...]} 형태의 그래프
graph = [[] for _ in range(V + 1)]
# u: 출발 정점, v: 도착 정점, w: 간선의 가중치
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((w, v))

distance = dijkstra((0, K))
for distance in distance[1:]:
    print('INF' if distance == float('inf') else distance)